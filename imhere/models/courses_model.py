from model import Model
from datetime import datetime, date
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
        # uni = self.escape_string(uni)
        query = self.ds.query(kind='student')
        query.add_filter('uni', '=', uni)
        result = list(query.fetch())

        if len(result) == 1:
            # found a student with uni, attempt to add to enrolled_in
            sid = result[0]['sid']
            try:
                key = self.ds.key('enrolled_in')
                entity = datastore.Entity(
                    key=key)
                entity.update({
                    'sid': sid,
                    'cid': self.cid
                })
                self.ds.put(entity)
                return 0
            except:
                # failed because already in enrolled_in
                return -2
        else:
            # invalid uni
            return -1

    def remove_student(self, uni):
        uni = self.escape_string(uni)
        query = "select sid from students where uni = '%s'" % uni
        result = self.db.execute(query)

        if result.rowcount == 1:
            # found a student with uni, attempt to remove from enrolled_in
            sid = result.fetchone()[0]

            query = ('select * from enrolled_in '
                     'where sid = %s and cid = %s'
                     % (sid, self.cid))
            result = self.db.execute(query)

            if result.rowcount == 1:
                query = 'delete from enrolled_in where sid = %s and cid = %s' \
                        % (sid, self.cid)
                self.db.execute(query)

                query = ('delete from attendance_records using sessions '
                         'where attendance_records.seid = sessions.seid '
                         'and attendance_records.sid = %s '
                         'and sessions.cid = %s'
                         % (sid, self.cid))
                self.db.execute(query)
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
        self.cid = self.escape_string(self.cid)
        query = ('select seid from sessions '
                 'where cid = %s '
                 "and expires > '%s' "
                 "and day >= '%s'"
                 % (self.cid, self.now, self.today))
        result = self.db.execute(query)
        return result.fetchone()[0] if result.rowcount == 1 else -1

    def close_session(self, seid):
        if seid == -1:
            return

        query = ('update sessions '
                 "set expires = '%s' "
                 'where seid = %s'
                 % (self.now, seid))
        self.db.execute(query)

        self.cid = self.escape_string(self.cid)
        query = 'update courses set active = 0 where cid = %s' % self.cid
        self.db.execute(query)

    def open_session(self):
        '''Opens a session for this course
        and returns the secret code for that session.
        '''
        # auto-generated secret code for now
        randsecret = randint(1000, 9999)
        self.cid = self.escape_string(self.cid)
        query = ('insert into sessions (cid, secret, expires, day) '
                 "values (%s, '%d', '%s', '%s')"
                 % (self.cid, randsecret, '23:59:59', self.today))
        self.db.execute(query)

        query = 'update courses set active = 1 where cid = %s' % self.cid
        self.db.execute(query)
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
