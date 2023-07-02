import unittest
from unittest.mock import MagicMock, patch
import socket

from mymodule import get_local_ip

class TestGetLocalIP(unittest.TestCase):
    @patch('socket.socket')
    def test_get_local_ip(self, mock_socket):
        mock_socket.return_value.getsockname.return_value = ('192.168.1.2', 1234)
        mock_socket.return_value.connect.return_value = None
        mock_socket.return_value.getsockname.return_value = ('192.168.1.2', 1234)
        mock_socket.return_value.gethostbyaddr.return_value = ('myhostname.local', [], ['192.168.1.2'])
        result = get_local_ip()
        self.assertEqual(result, '192.168.1.2')