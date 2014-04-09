# test cases for dumponus

import unittest
import dumponus


class DumponUsTest(unittest.TestCase):

    def setUp(self):
        dumponus.config['TESTING'] = True
        dumponus.config['CSRF_ENABLED'] = False
        self.app = dumponus.test_client()

    def tearDown(self):
        dumponus.db.session.remove()
        dumponus.db.drop_all()

    def test_unique_photo_name(self):
        pass


if __name__ == "__main__":
     unittest.main()