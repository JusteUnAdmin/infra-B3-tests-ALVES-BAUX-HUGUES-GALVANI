#nous avons créé deux cas de test: test_scan_with_internet et test_scan_without_internet. Dans le premier cas, nous simulons une connexion Internet réussie en utilisant patch pour remplacer la fonction urlopen par une fonction de simulation. Nous vérifions que la fonction print est appelée avec les valeurs attendues #pour local_ip et subnet.

#Dans le deuxième cas, nous simulons une absence de connexion Internet en faisant urlopen pour lancer une exception. Nous vérifions que la fonction print est appelée avec la chaîne "Pas de connexion Internet\n".

import unittest
from unittest.mock import patch
from io import StringIO
from your_module import YourClass

class TestYourClass(unittest.TestCase):

    def setUp(self):
        self.obj = YourClass()

    @patch('builtins.print')
    @patch('urllib.request.urlopen')
    def test_scan_with_internet(self, mock_urlopen, mock_print):
        mock_urlopen.return_value = True
        self.obj.scan()
        self.assertTrue(mock_print.called_with(local_ip))
        self.assertTrue(mock_print.called_with(subnet))

    @patch('builtins.print')
    @patch('urllib.request.urlopen')
    def test_scan_without_internet(self, mock_urlopen, mock_print):
        mock_urlopen.side_effect = Exception("Pas de connexion Internet")
        self.obj.scan()
        self.assertTrue(mock_print.called_with("Pas de connexion Internet\n"))

if __name__ == '__main__':
    unittest.main()
