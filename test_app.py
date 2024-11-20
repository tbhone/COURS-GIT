"""Module de test pour la fonction inverser_chaine du module app."""

import unittest
from app import inverser_chaine

class TestInverserChaine(unittest.TestCase):
    """Tests pour la fonction inverser_chaine."""

    def test_inverser_chaine_correct(self):
        """Test les cas où la fonction devrait réussir."""
        self.assertEqual(inverser_chaine("bonjour"), "ruojnob")
        self.assertEqual(inverser_chaine("abcd"), "dcba")
        self.assertEqual(inverser_chaine(""), "")
        self.assertEqual(inverser_chaine("a"), "a")
        self.assertEqual(inverser_chaine("12321"), "12321")

    def test_inverser_chaine_incorrect(self):
        """Test un cas où la fonction ne se comporte pas comme prévu."""
        self.assertNotEqual(inverser_chaine("bonjour"), "jourbon")

if __name__ == "__main__":
    unittest.main()
