from model import Model
from datetime import datetime, date
from google.cloud import datastore

class Students(Model):

    def __init__(self, sid):
        self.sid = sid
        self.ds = self.get_client()

    def get_uni(self):
        query = self.ds.query(kind='student')
        query.add_filter('sid', '=', self.sid)
        result = list(query.fetch())
        return result[0]['uni']

    def get_courses(self):
        query = self.ds.query(kind='enrolled_in')
        query.add_filter('sid', '=', self.sid)
        enrolledCourses = list(query.fetch())
        result = list()
        for enrolledCourse in enrolledCourses:
            query = self.ds.query(kind='courses')
            query.add_filter('cid', '=', enrolledCourse['cid'])
            result = result + list(query.fetch())

        return result

    def get_secret_and_seid(self):
        now = datetime.time(datetime.now())
        today = date.today()

        try:
            query = ('select secret, seid '
                     'from sessions, enrolled_in '
                     'where enrolled_in.sid = %s '
                     'and enrolled_in.cid = sessions.cid '
                     "and sessions.expires > '%s' "
                     "and sessions.day >= '%s'"
                     % (self.sid, now, today))
            result = self.db.execute(query)
            row = result.fetchone()
            secret = row[0]
            seid = row[1]
        except:
            secret, seid = None, -1

        return secret, seid

    def has_signed_in(self):
        _, seid = self.get_secret_and_seid()

        if seid == -1:
            return False
        else:

            query = ('select * from attendance_records, sessions '
                     'where attendance_records.seid = sessions.seid '
                     'and attendance_records.sid = %s '
                     'and sessions.seid = %s'
                     % (self.sid, seid))
            result = self.db.execute(query)
            return True if result.rowcount == 1 else False

    def insert_attendance_record(self, seid):
        query = 'insert into attendance_records values (%s, %s)' \
                % (self.sid, seid)
        self.db.execute(query)

    def get_num_attendance_records(self, cid):
        # query = ('select * '
        #          'from attendance_records, sessions '
        #          'where attendance_records.seid = sessions.seid '
        #          'and sessions.cid = %s '
        #          'and attendance_records.sid = %s'
        #          % (cid, self.sid))
        # result = self.db.execute(query)
        # return result.rowcount

        query = self.ds.query(kind='sessions')
        query.add_filter('cid', '=', int(cid))
        sessions = list(query.fetch())
        results = list()
        for session in sessions:
            query = self.ds.query(kind='attendance_records')
            query.add_filter('seid', '=', session['seid'])
            query.add_filter('sid', '=', self.sid)
            results = results + list(query.fetch())
        return len(results)
