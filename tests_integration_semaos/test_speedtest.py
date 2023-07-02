import unittest
from unittest.mock import MagicMock, patch

from mymodule import resultat_speedtest

class TestResultatSpeedtest(unittest.TestCase):
    @patch('builtins.open', new_callable=MagicMock)
    def test_resultat_speedtest(self, mock_open):
        mock_file = MagicMock(spec=open)
        mock_file.__enter__.return_value.readline.side_effect = ['Download speed: 50 Mbps\n', 'Upload speed: 25 Mbps\n']
        mock_open.return_value = mock_file
        result = resultat_speedtest()
        self.assertEqual(result, ' 50 Mbps\n 25 Mbps')