import unittest
 
from translator import englishToFrench,frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench(' '), 'Bonjour')


class TestFrenchToEnglish(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish(' '), 'Hello')

unittest.main()