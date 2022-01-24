from flask_testing import TestCase
from flask import current_app,url_for
from main import app

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        
        return app

    def test_app_create(self):
        self.assertIsNotNone(current_app)


    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])


    def test_client(self):
       response = self.client.get("/")
       self.assertEquals(response.json, dict(Message='Welcome to API REST Python myDenue'))