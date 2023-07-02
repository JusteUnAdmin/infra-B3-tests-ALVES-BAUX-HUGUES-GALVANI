import unittest
from unittest.mock import patch
from app import app

class TestAgent(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('requests.get')
    def test_agent_success(self, mock_get):
        mock_get.side_effect = [
            MockResponse({'local_ip': '192.168.1.1', 'time_ping': 10, 'ip': '127.0.0.1', 'download': 100, 'upload': 50, 'Hostname': 'localhost'}),
            MockResponse({'ips': ['192.168.1.1', '192.168.1.2'], 'hostnames': ['localhost', 'test'], 'ports': [80, 443]})
        ]
        response = self.app.get('/agent/127.0.0.1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'localhost', response.data)
        self.assertIn(b'192.168.1.1', response.data)
        self.assertIn(b'80', response.data)

    @patch('requests.get')
    def test_agent_failure(self, mock_get):
        mock_get.side_effect = Exception()
        response = self.app.get('/agent/127.0.0.1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Aucune information disponible', response.data)

class MockResponse:
    def __init__(self, json_data, status_code=200):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data
    
if __name__ == '__main__':
    unittest.main()
