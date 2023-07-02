import unittest
from unittest.mock import MagicMock, patch

from mymodule import ping

class TestPing(unittest.TestCase):
    @patch('os.popen')
    def test_ping_success(self, mock_popen):
        mock_popen.return_value.read.return_value = 'PING google.com (173.194.203.100): 56 data bytes\n64 bytes from 173.194.203.100: icmp_seq=0 ttl=57 time=11.231 ms\n\n--- google.com ping statistics ---\n1 packets transmitted, 1 packets received, 0.0% packet loss\nround-trip min/avg/max/stddev = 11.231/11.231/11.231/0.000 ms\n'
        ping()
        self.assertEqual(time_ping, 11.231)

    @patch('os.popen')
    def test_ping_failure(self, mock_popen):
        mock_popen.return_value.read.return_value = 'Ping request could