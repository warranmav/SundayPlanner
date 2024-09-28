import unittest
from datetime import datetime
from flask import Flask
from flask_testing import TestCase
from app import create_app, db
from app.models import User, Speaker, Assignment

class AssignSpeakerTestCase(TestCase):

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
        speaker = Speaker(name='John Doe', topic='Faith')
        db.session.add(speaker)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_assign_speaker(self):
        response = self.client.post('/assign_speaker', data=dict(
            speaker_id=1,
            date='2024-10-06',  # Ensure this is a Sunday
            duration='10 Min',
            order='1'
        ))
        self.assertEqual(response.status_code, 302)  # Redirect after successful assignment
        assignment = Assignment.query.first()
        self.assertIsNotNone(assignment)
        self.assertEqual(assignment.speaker_id, 1)
        self.assertEqual(assignment.date, datetime.strptime('2024-10-06', '%Y-%m-%d').date())
        self.assertEqual(assignment.duration, '10 Min')
        self.assertEqual(assignment.order, 1)

    def test_assign_speaker_non_sunday(self):
        response = self.client.post('/assign_speaker', data=dict(
            speaker_id=1,
            date='2024-10-05',  # Ensure this is not a Sunday
            duration='10 Min',
            order='1'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Assignment date must be a Sunday', response.data)

if __name__ == '__main__':
    unittest.main()
