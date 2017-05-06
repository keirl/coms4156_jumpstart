from google.cloud import datastore
from flask import current_app

class Model:

    def get_client(self): # TODO fix the config file
        #return datastore.Client(current_app.config['PROJECT_ID'])
        return datastore.Client('cu-ase')