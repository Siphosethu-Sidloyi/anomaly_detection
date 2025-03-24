import unittest
from app import app

class CalculatorAPITestCase(unittest.TestCase):
    def setUp(self):
        # Configure the app for testing and create a test client.
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_add(self):
        response = self.client.get('/add?a=10&b=20')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data.get('result'), 30)

    def test_subtract(self):
        response = self.client.get('/subtract?a=20&b=10')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data.get('result'), 10)

    def test_multiply(self):
        response = self.client.get('/multiply?a=5&b=3')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data.get('result'), 15)

    def test_divide(self):
        response = self.client.get('/divide?a=20&b=5')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data.get('result'), 4)

    def test_divide_by_zero(self):
        response = self.client.get('/divide?a=20&b=0')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('error', data)

    def test_invalid_input(self):
        response = self.client.get('/add?a=foo&b=bar')
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()
