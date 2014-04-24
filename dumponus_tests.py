# test cases for dumponus

import datetime
import unittest
import dumponus
from pyhashxx import hashxx
from flask import json
from models import Photo
from werkzeug import secure_filename


class DumponUsTest(unittest.TestCase):

    def setUp(self):
        self.date = str(datetime.datetime.now())
        self.uuid = str(hashxx(secure_filename('wut.jpg') + self.date))
        self.formatted_image = {'data': {
            "id": self.uuid,
            "title": "Monkey Socks",
            "type": "image/jpeg",
            "creation_date": self.date,
            "size": 52191,
            "url": "http://dumpon.us/imgs/" + self.uuid + '.jpg'
        }, 'status': 200 }
        self.image_keys = ['id', 'title', 'type', 'creation_date', 'size', 'url']
        self.json_image = json.dumps(self.formatted_image)
        self.app = dumponus.app.test_client()
        self.image_model = Photo('wut.jpg', 'Monkey Socks', 'image/jpeg', 52191, "http://dumpon.us/imgs/" + self.uuid + '.jpg', creation_date=self.date)
        self.db = dumponus.db
        #keep track of ids (they are changing) and delete test data on tearDown
        self.ids = []
        self.images = []

    def test_image_model_data_is_dict(self):
        """ Image model is a dict """
        self.assertIsInstance(self.image_model.data, dict)
        
    def test_image_model_equals_formatted_image(self):
        """ Image data and test dict should be the same """
        self.assertEqual(self.image_model.data, self.formatted_image)

    def test_save_successful(self):
        """ Passes if the model save (sends to db) was successful """
        self.ids.append(self.image_model.get_id())
        self.images.append(self.image_model.data['data'])
        self.assertTrue(self.image_model.save())

    def test_throw_type_error_on_less_values(self):
        """ Throws a TypeError if not enough params provided to the image model """
        self.assertRaises(TypeError, Photo, 'testy', 'shit')


    def test_unique_photo_name(self):
        """ Passes if the photos do not get assigned the same id """
        i = Photo('wut.jpg', 'Monkey Socks', 'image/jpeg', 52191, datetime.datetime.now())
        self.assertNotEqual(self.image_model.get_id(), i.get_id())

    def test_validate_dict_fields(self):
        """ All of the dictionary keys have to match the json model """
        keys = self.image_model.data.keys()
        self.assertEqual(keys.sort(), self.image_keys.sort())


    def test_validate_static_image_url(self):
        """ Static image url should have proper extensions, etc """
        pass

    
    def test_get_photo(self):
        """ Make a GET to api/images/{image_id} and retrieve the necessary success codes """
        self.image_model.save()
        self.ids.append(self.image_model.data['data']['id'])
        self.images.append(self.image_model.data['data'])
        resp = self.app.get('/api/images/'+self.image_model.get_id())
        obj_representation = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.mimetype, 'application/json')
        self.assertEqual(resp.data, self.json_image)
        self.assertIsInstance(obj_representation, dict)
        self.assertEqual(obj_representation.keys().sort(), self.image_keys.sort())

    
    def test_404_on_get(self):
        """ Make a GET to api/images, providing a bad id """
        resp = self.app.get('/api/images/' + '1234')
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(resp.status, '404 NOT FOUND')


    def test_get_photos(self):
        """ Make a GET to api/images and retrieve list of images """
        self.image_model.save()
        resp = self.app.get('/api/images')
        obj_representation = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.mimetype, 'application/json')
        self.assertIsInstance(obj_representation, dict)
        self.assertIsInstance(obj_representation['data'], list)


    def test_validate_post_params(self):
        """ Makes sure post parameters are correct """
        pass

    def test_post_and_upload_photo(self):
        """ Make a POST to api/images with the required params """
        pass

    def test_photo_fail_no_image(self):
        """ Fail by no image being passed through image parameter """
        pass

    def tearDown(self):
        pipe = self.db.pipeline()
        for i in self.ids:
            pipe.delete(i)
        for i in self.images:
            pipe.lrem('data', 1, i)
        pipe.execute()
        

if __name__ == "__main__":
    unittest.main()
