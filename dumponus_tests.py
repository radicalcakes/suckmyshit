# test cases for dumponus

import datetime
import unittest
import dumponus
from models import Image
from werkzeug import secure_filename


class DumponUsTest(unittest.TestCase):

    def setUp(self):
        dumponus.config['TESTING'] = True
        dumponus.config['CSRF_ENABLED'] = False
        self.formatted_image = {
            "id": "193327862177839940",
            "type": "image/jpeg",
            "creation_date": "2014-04-09 19:31:53.355174",
            "size": 521916,
            "url": "http://dumpon.us/imgs/193327862177839940.jpg"
        }
        self.app = dumponus.test_client()
        self.db = dumponus.db

    def test_image_model(self):
        """ Image model is a dict """
        # i = Image('wut.jpg')
        pass

    def tearDown(self):
        """ Delete the test object from the database """
        pass

    def test_unique_photo_name(self):
        pass

    def test_get_photo(self):
        """ Make a GET to api/images/{image_id} and retrieve the necessary success codes """
        pass

    def test_post_photo(self):
        """ Make a POST to api/images """
        pass



if __name__ == "__main__":
    unittest.main()
