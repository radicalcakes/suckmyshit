import datetime
import UserDict
from werkzeug import secure_filename


class Image(UserDict.UserDict):
    """ Save image data as a dictionary. Access the dictionary with img = new Image() img['data'] """
    def __init__(self, name, typ, creation_date=datetime.datetime.now(), size=None, url=None):
        self.type = typ
        self.creation_date = creation_date
        self.size = size
        self.url = url
        self.id = self.__create_id(name, creation_date)
        
    def create_id(self, name, creation_date):
        return str(hash(secure_filename(name) + str(creation_date)))

    __create_id = create_id

