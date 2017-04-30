from model import Model
from google.cloud import datastore

class Users(Model):

    def get_client():
        return datastore.Client(current_app.config['PROJECT_ID'])

    def get_or_create_user(self, user):
        try:
            # insert = """
            # INSERT INTO users (name, family_name, email)
            # VALUES ('{0}', '{1}', '{2}')
            # """.format(user['given_name'], user['family_name'], user['email'])
            #
            # self.db.execute(insert)
            ds = get_client()
            key = ds.key('user')
            entity = datastore.Entity(
                key=key)
            entity.update(user)
            ds.put(entity)
        except:  # TODO
            pass

        # query = """
        # SELECT uid FROM users WHERE email = '{0}'
        # """.format(user['email'])
        query = ds.query(kind='user')
        query.add_filter('email', '=', user['email'])

        # result = self.db.execute(query)
        result = list(query.fetch())
        return self.deproxy(result)[0]['uid']

    def is_valid_uni(self, uni):
        uni = self.escape_string(uni)
        query = "select sid from students where uni = '%s'" % uni
        result = self.db.execute(query)
        return True if result.rowcount == 1 else False
