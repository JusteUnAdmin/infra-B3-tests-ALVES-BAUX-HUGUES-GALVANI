import unittest
from unittest.mock import MagicMock, patch

from mymodule import get_public_ip

class TestGetPublicIP(unittest.TestCase):
    @patch('requests.get')
    def test_get_public_ip(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = '192.168.1.2'
        mock_get.return_value = mock_response
        result = get_public_ip()
        self.assertEqual(result, '192.168.1.2')