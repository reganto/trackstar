from unittest import TestCase
from flask import current_app
from trackstar import create_app, db


class ConnectionToDBTestCase(TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config["TESTING"])

    def test_db_track_modifications(self):
        self.assertFalse(current_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"])

    def test_connection_to_db(self):
        self.assertIsNotNone(db.session.connection())

    
