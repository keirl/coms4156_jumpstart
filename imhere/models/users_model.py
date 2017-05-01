from model import Model
from google.cloud import datastore

class Users(Model):

    def get_or_create_user(self, user):
        ds = self.get_client()
        query = ds.query(kind='user')
        query.add_filter('email', '=', user['email'])

        result = list(query.fetch())
        if result:
            print result
        else:
            try:
                key = ds.key('user')
                entity = datastore.Entity(
                    key=key)
                entity.update(user)
                ds.put(entity)
                # key2 = ds.key('user', int('5715999101812736'))
                # ds.delete(key2)
            except:  # TODO
                pass
        result = list(query.fetch())
        return result[0]['id']


    def is_valid_uni(self, uni): # TODO convert to datastore
        uni = self.escape_string(uni)
        query = "select sid from students where uni = '%s'" % uni
        result = self.db.execute(query)
        return True if result.rowcount == 1 else False
