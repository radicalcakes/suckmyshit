import datetime
from pyhashxx import hashxx
from flask import json
from dumponus import db, uploaded_photos
from werkzeug import secure_filename


class Photo(object):
    """ Save image data as a dictionary. Access the dictionary with img = new Image() img['data'] """
    def __init__(self, name, title, typ, size,  url=None, creation_date=datetime.datetime.now()):
        self.type = typ
        self.title = title
        self.creation_date = creation_date
        self.size = size
        self.url = url
        self.data = {}
        self.make_id(name, creation_date)
        self.__to_dict()

    def make_id(self, name, creation_date):
        self.__id = str(hashxx(secure_filename(name) + str(creation_date)))
    
    def get_id(self):
        return self.__id

    def to_dict(self):
        """ creates a dictionary object  should be used privately but can be exposed """
        self.data['type'] = self.type
        self.data['title'] = self.title
        self.data['creation_date'] = self.creation_date
        self.data['size'] = self.size
        self.data['url'] = self.url
        self.data['id'] = self.get_id()
    
    __to_dict = to_dict

    @property
    def make_url(self):
        return uploaded_photos.url(self.id)

    def save(self):
        print db.set(self.get_id(), self.data)
        return db.set(self.get_id(), self.data)
        
        

