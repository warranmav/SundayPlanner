import unittest
from app import create_app, db
from app.models import Speaker
from tests.helpers import create_test_user

class SpeakersTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('config.TestConfig')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        create_test_user(self.client)
        self.speaker = Speaker(name='John Doe', topic='Faith')
        db.session.add(self.speaker)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_speakers_page(self):
        response = self.client.get('/speakers')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Doe', response.data)
        self.assertIn(b'Faith', response.data)

if __name__ == '__main__':
    unittest.main()
