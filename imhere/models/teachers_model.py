from model import Model
from datetime import datetime, date
from google.cloud import datastore

class Teachers(Model):

    def __init__(self, tid):
        self.tid = tid
        self.now = datetime.now()
        self.today = datetime.today()

    def get_courses(self):
        query = ('select courses.cid, courses.name '
                 'from courses, teaches '
                 'where courses.cid = teaches.cid '
                 'and teaches.tid = %s'
                 % self.tid)
        result = self.db.execute(query)
        return self.deproxy(result)

    def get_courses_with_session(self):
        ds = self.get_client()
        query = ds.query(kind='teaches')
        query.add_filter('tid', '=', self.tid)
        teaches = list(query.fetch())
        courses = list()
        for teach in teaches:
            query = ds.query(kind='courses')
            query.add_filter('cid', '=', teach['cid'])
            courses = courses + list(query.fetch())
        result = list()
        for course in courses:
            print "here are some courses!!!!!!!! " + str(course)
            query = ds.query(kind='sessions')
            query.add_filter('cid', '=', course['cid'])
            query.add_filter('expires', '>', self.now)
            # query.add_filter('day', '>=', self.today)
            result = result + list(query.fetch())

        return result


    def add_course(self, course_name):
        ds = self.get_client()
        key = ds.key('courses')
        entity = datastore.Entity(
            key=key)
        entity.update({
            'name': course_name,
            'active': 0
        })
        ds.put(entity)
        cid = entity.key.id
        entity.update({
            'cid': cid
        })
        ds.put(entity)

        key = ds.key('teaches')
        entity = datastore.Entity(
            key=key)
        entity.update({
            'tid': self.tid,
            'cid': cid
        })
        ds.put(entity)
        return cid

    def remove_course(self, cid):
        cid = self.escape_string(cid)
        query = 'delete from courses where cid = %s' % cid
        self.db.execute(query)
