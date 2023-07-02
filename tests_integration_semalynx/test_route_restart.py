#On simule une requète POST sur l'URL "/restart_agent" et on vérifie que le message de réussite apparait, dans le second test, nous testons le même processur avec une erreur

import unittest
from unittest.mock import patch
from app import app

class TestRestartAgent(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('requests.post')
    def test_restart_agent_success(self, mock_post):
        mock_post.return_value.ok = True
        response = self.app.post('/restart_agent', data=dict(agent_ip='127.0.0.1'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, 'http://localhost]/')

    @patch('requests.post')
    def test_restart_agent_failure(self, mock_post):
        mock_post.side_effect = Exception()
        response = self.app.post('/restart_agent', data=dict(agent_ip='[IP_AGENT]'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, 'http://[IP_AGENT]/')
    
if __name__ == '__main__':
    unittest.main()
