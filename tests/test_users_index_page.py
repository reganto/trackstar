from unittest import TestCase
from trackstar import create_app


class UserIndexPageTestCase(TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_users_index_page(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("users" in response.get_data(as_text=True))

