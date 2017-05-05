# Sources:
# https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/appengine/standard/localtesting/datastore_test.py
# http://flask.pocoo.org/docs/0.12/testing/

import os
import imhere
import unittest
import tempfile
from flask import session

import sys
sys.path.insert(1, 'google-cloud-sdk/platform/google_appengine')
sys.path.insert(1, 'google-cloud-sdk/platform/google_appengine/lib/yaml/lib')
sys.path.insert(1, 'myapp/lib')

from google.appengine.api import memcache
from google.appengine.ext import ndb
from google.appengine.ext import testbed



class StaticTestCase(unittest.TestCase):

    def setUp(self):
#        self.db_fd, imhere.app.config['DATABASE'] = tempfile.mkstemp()
        imhere.app.config['TESTING'] = True
        imhere.app.secret_key = 'dude'
        self.app = imhere.app.test_client()
#        with imhere.app.app_context():
#            imhere.init_db()

    def tearDown(self):
#        os.close(self.db_fd)
#        os.unlink(imhere.app.config['DATABASE'])
        pass

    def test_index(self):
        rv = self.app.get('/')
        assert b'Register' in rv.data
        assert b'ImHere' in rv.data

class RegistrationTestCase(unittest.TestCase):

    #http://stackoverflow.com/questions/35470357/cant-get-session-variables-set-up-in-flask-unit-test
    #http://stackoverflow.com/questions/20272083/flask-unittesting-session-decorator
    def test_registration(self):
        with imhere.app.test_client() as client:
            client.secret_key = 'dude'            
            with client.session_transaction() as sess:
                sess['google_user'] = {'name':'Dude'}
                sess['is_student'] = True
                sess['is_teacher'] = False
            rv = self.app.get('/register')
            assert b'Registration' in rv.data   

   
    #def test_login(self):
     #   rv = self.app.get('/register')

#    def preprocess_request(self):
 #       imhere.app.secret_key = 'dude'
        

  #  with imhere.app.test_request_context('/register'):
   #     imhere.app.preprocess_request()
    #    assert b'Registration' in rv.data
        

       


if __name__ == '__main__':
    unittest.main()
