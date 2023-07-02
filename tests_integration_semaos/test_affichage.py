import unittest
from unittest.mock import mock_open, patch

class TestDisplayResults(unittest.TestCase):

    def test_display_results(self):
        file_content = "192.168.0.1\thostname1\t80,443\n192.168.0.2\thostname2\t22\n"

        with patch('builtins.open', mock_open(read_data=file_content)):
            result_text = tk.Text()
            display_results(result_text)

            expected_output = "\n192.168.0.1         hostname1                      80,443\n\n192.168.0.2         hostname2                      22\n"
            self.assertEqual(result_text.get("1.0", tk.END), expected_output)

    def test_display_results_file_not_found(self):
        with patch('builtins.open', side_effect=FileNotFoundError()):
            result_text = tk.Text()
            display_results(result_text)

            expected_output = "Aucun résultat de scan réseau n'a été trouvé.\n"
            self.assertEqual(result_text.get("1.0", tk.END), expected_output)



