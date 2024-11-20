import unittest
from app import inverser_chaine

class TestInverserChaine(unittest.TestCase):
    def test_inverser_chaine(self):
        #ici je fais un test qui fonctionne
        self.assertEqual(inverser_chaine("bonjour"), "ruojnob")
        self.assertEqual(inverser_chaine("abcd"), "dcba")
        self.assertEqual(inverser_chaine(""), "")
        self.assertEqual(inverser_chaine("a"), "a")
        self.assertEqual(inverser_chaine("12321"), "12321")
    #ici je fais un test qui ne fonctionne pas
    def test_inverser_chaine(self):
        self.assertEqual(inverser_chaine("bonjour"), "jourbon")
        self.assertEqual(inverser_chaine("abcd"), "dcba")
        self.assertEqual(inverser_chaine(""), "")
        self.assertEqual(inverser_chaine("a"), "a")
        self.assertEqual(inverser_chaine("12321"), "12321")

if __name__ == "__main__":
    unittest.main()
