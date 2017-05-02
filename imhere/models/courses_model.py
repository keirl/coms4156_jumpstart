from model import Model
from datetime import datetime, date, timedelta
from random import randint
from google.cloud import datastore

class Courses(Model):

    def __init__(self, cid=-1):
        self.cid = cid
        self.now = datetime.time(datetime.now())
        self.today = date.today()
        self.ds = self.get_client()

    def get_course_name(self):
        query = self.ds.query(kind='courses')
        query.add_filter('cid', '=', int(self.cid))
        result = list(query.fetch())
        return result[0]['name']

    def get_students(self):
        query = self.ds.query(kind='enrolled_in')
        query.add_filter('cid', '=', int(self.cid))
        enrolledIn = list(query.fetch())
        results = list()
        for enrolled in enrolledIn:
            query = self.ds.query(kind='user')
            query.add_filter('id', '=', enrolled['sid'])
            results = results + list(query.fetch())
        return results

    def add_student(self, uni):
        query = self.ds.query(kind='student')
        query.add_filter('uni', '=', uni)
        result = list(query.fetch())

        if len(result) == 1:
            # found a student with uni, attempt to add to enrolled_in
            sid = result[0]['sid']
            query = self.ds.query(kind='enrolled_in')
            query.add_filter('sid', '=', sid)
            query.add_filter('cid', '=', int(self.cid))
            result = list(query.fetch())
            print "enrolled " + str(result)
            if len(result) > 0:
                # failed because already in enrolled_in
                return -2

            key = self.ds.key('enrolled_in')
            entity = datastore.Entity(
                key=key)
            entity.update({
                'sid': sid,
                'cid': int(self.cid)
            })
            self.ds.put(entity)
            query = self.ds.query(kind='enrolled_in')
            teaches = list(query.fetch())
            print teaches
            return 0

        else:
            # invalid uni
            return -1

    def remove_student(self, uni):
        query = self.ds.query(kind='student')
        query.add_filter('uni', '=', uni)
        result = list(query.fetch())

        if len(result) == 1:
            # found a student with uni, attempt to remove from enrolled_in
            sid = result[0]['sid']

            query = self.ds.query(kind='enrolled_in')
            query.add_filter('sid', '=', sid)
            query.add_filter('cid', '=', int(self.cid))
            result = list(query.fetch())

            if len(result) > 0:

                self.ds.delete(result[0].key)

                query = self.ds.query(kind='sessions')
                query.add_filter('cid', '=', int(self.cid))
                sessions = list(query.fetch())
                print sessions
                attendanceRecords = list()
                for session in sessions:
                    query = self.ds.query(kind='attendance_records')
                    query.add_filter('seid', '=', int(session['seid']))
                    attendanceRecords = attendanceRecords + list(query.fetch())
                print attendanceRecords
                for attendanceRecord in attendanceRecords:
                    self.ds.delete(attendanceRecord.key)
                return 0
            else:
                # failed because it was not in enrolled_in to begin with
                return -3
        else:
            # invalid uni
            return -1

    def get_active_session(self):
        '''Return the seid of an active session if it exists,
        otherwise return -1.
        '''
        # query = ('select seid from sessions '
        #          'where cid = %s '
        #          "and expires > '%s' "
        #          "and day >= '%s'"
        #          % (self.cid, self.now, self.today))
        # result = self.db.execute(query)
        # return result.fetchone()[0] if result.rowcount == 1 else -1
        # TODO fix expiration
        query = self.ds.query(kind='sessions')
        query.add_filter('cid', '=', int(self.cid))
        sessions = list(query.fetch())
        print "here are the sessions " + str(sessions)
        return sessions[0]['seid'] if len(sessions) == 1 else -1

    def close_session(self, seid):
        if seid == -1:
            return

        # query = ('update sessions '
        #          "set expires = '%s' "
        #          'where seid = %s'
        #          % (self.now, seid))
        # self.db.execute(query)

        query = self.ds.query(kind='sessions')
        query.add_filter('seid', '=', int(seid))
        entity = list(query.fetch())[0]
        entity.update({
            'expires': datetime.now()
        })
        self.ds.put(entity)

        # TODO fix expiration

        # query = 'update courses set active = 0 where cid = %s' % self.cid
        # self.db.execute(query)

        query = self.ds.query(kind='courses')
        query.add_filter('cid', '=', int(self.cid))
        entity = list(query.fetch())[0]
        entity.update({
            'active': 0
        })
        self.ds.put(entity)


    def open_session(self):
        '''Opens a session for this course
        and returns the secret code for that session.
        '''
        # auto-generated secret code for now
        randsecret = randint(1000, 9999)
        # query = ('insert into sessions (cid, secret, expires, day) '
        #          "values (%s, '%d', '%s', '%s')"
        #          % (self.cid, randsecret, '23:59:59', self.today))
        # self.db.execute(query)

        key = self.ds.key('sessions')
        entity = datastore.Entity(
            key=key)
        entity.update({
            'cid': int(self.cid),
            'secret': int(randsecret),
            'expires': datetime.now() + timedelta(days=1)
            # 'day': self.today
        })
        self.ds.put(entity)
        seid = entity.key.id
        entity.update({
            'seid': seid
        })
        self.ds.put(entity)
        query = self.ds.query(kind='sessions')
        sessions = list(query.fetch())
        print "here are the sessions!!!!!!!!!!! " + str(sessions)

        # query = 'update courses set active = 1 where cid = %s' % self.cid
        # self.db.execute(query)
        print "here is the cid being updated " + str(self.cid)
        key = self.ds.key('courses', int(self.cid))
        results = self.ds.get(key)
        entity = datastore.Entity(
            key=key)
        entity.update({
            'name': results['name'],
            'active': 1,
            'cid': results['cid']
        })
        self.ds.put(entity)
        query = self.ds.query(kind='courses')
        teaches = list(query.fetch())
        print "here are the courses !!!!!!!!!!!!!! " + str(teaches)

        return randsecret

    def get_secret_code(self):
        query = self.ds.query(kind='courses')
        query.add_filter('cid', '=', int(self.cid))
        courses = list(query.fetch())
        results = list()
        for course in courses:
            query = self.ds.query(kind='sessions')
            query.add_filter('cid', '=', course['cid'])
            # TODO datastore fix sessions
            # query.add_filter('expires', '>', self.now)
            # query.add_filter('day', '>=', self.today)
            results = results + list(query.fetch())
        return results[0] if len(results) == 1 else None

    def get_num_sessions(self):
        query = self.ds.query(kind='sessions')
        query.add_filter('cid', '=', int(self.cid))
        results = list(query.fetch())
        return len(results)
