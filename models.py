import datetime
from dumponus import db


class Photo(object):
    """ Save image data as a dictionary. Access the dictionary with img = new Image() img['data'] """
    def __init__(self, name, typ, size, url, title=None, creation_date=datetime.datetime.now()):
        self.type = typ
        self.title = title
        self.creation_date = creation_date
        self.size = size
        self.url = url
        self.data = {'data': {}}
        self.make_id(name)
        self.__to_dict()

    def make_id(self, name):
        self.__id = name.split('.')[0]
    
    def get_id(self):
        return self.__id

    def to_dict(self):
        """ creates a dictionary object  should be used privately but can be exposed """
        self.data['data']['type'] = self.type
        self.data['data']['title'] = self.title
        self.data['data']['creation_date'] = self.creation_date
        self.data['data']['size'] = self.size
        self.data['data']['url'] = self.url
        self.data['data']['id'] = self.get_id()
        self.data['status'] = 200
    
    __to_dict = to_dict

    def save(self):
        """ saves to redis with the id as the key, also adds the object to a list saved in an images dict """
        #returns true or false if the operations complete
        
        saved_to_db = db.set(self.get_id(), self.data) and db.rpush('data', self.data['data'])
        return saved_to_db
        

