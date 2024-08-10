import unittest
from app import app  

class FlaskTest(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.content_type,'text/html; charset=utf-8')

    def test_non_existent_route(self):
        tester = app.test_client(self)
        response = tester.get('/non-existent')
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)

if __name__ == "__main__":
    unittest.main()

