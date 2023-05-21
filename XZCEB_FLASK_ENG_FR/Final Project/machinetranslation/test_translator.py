import unittest

from translator1 import english_to_french, french_to_english

class test_en2fr(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour") 
        self.assertNotEqual(english_to_french("Hello"),"roi")

class test_fr2en(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("roi"),"Hello") 

unittest.main()