#Le premier test vérifie que la fonction fonctionne correctement lorsque l'ordinateur est connecté à Internet, en vérifiant que la sortie contient les valeurs attendues pour le téléchargement et l'upload.

#Le deuxième test vérifie que la fonction gère correctement l'absence de connexion Internet, en vérifiant que la sortie contient le message "Pas de connexion Internet".

import unittest

class TestDebit(unittest.TestCase):
    def test_debit_with_internet(self):
        instance = MyClass()

        instance.test_debit()

        expected_output = "Test fini\nDownload: .* Mbps\nUpload: .* Mbps"
        self.assertRegex(instance.result_text.get(1.0, tk.END), expected_output)

    def test_debit_without_internet(self):
        instance = MyClass()
        instance.test_debit()

        
        expected_output = "Pas de connexion Internet"
        self.assertIn(expected_output, instance.result_text.get(1.0, tk.END))
