import unittest
from datetime import datetime, date
from flask import Flask
from flask_testing import TestCase
from app import create_app, db
from app.models import User, Speaker, Assignment

class AssignmentsPageTestCase(TestCase):

    def create_app(self):
        app = create_app('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        self.client = self.app.test_client()
        self.client.post('/register', data=dict(
            email='test@example.com',
            username='testuser',
            password='password'
        ))
        self.client.post('/login', data=dict(
            email='test@example.com',
            password='password'
        ))
        speaker = Speaker(name='John Doe')
        db.session.add(speaker)
        db.session.commit()
        assignment = Assignment(speaker_id=1, date=date(2024, 10, 6), duration='10 Min', order=1)
        db.session.add(assignment)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_assignments_page(self):
        response = self.client.get('/assignments')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Doe', response.data)
        self.assertIn(b'2024-10-06', response.data)
        self.assertIn(b'10 Min', response.data)
        self.assertIn(b'1st Speaker', response.data)

if __name__ == '__main__':
    unittest.main()
