import unittest
from start import get_synonyms, get_variations

class testGetSynonyms(unittest.TestCase):
    def test_synonyms(self):
        #test if synonyms are correct
        self.assertEqual(get_synonyms("#"),['Number'])
        self.assertItemsEqual(get_synonyms("ph"),['telephone', 'mobile', 'landline'])
        self.assertItemsEqual(get_synonyms(""),[])
        self.assertItemsEqual(get_synonyms("Hello"),[])
        #test for type errors
        self.assertRaises(TypeError, get_synonyms, 1)

    def test_variations(self):
        #test for variations
        self.assertItemsEqual(get_variations("ph #: +91-9848012345"),['mobile Number: +91-9848012345', 'telephone Number: +91-9848012345', 'landline Number: +91-9848012345'])
        self.assertItemsEqual(get_variations("NH #: 44"), ['National HighWay Number: 44'])

        #test for values
        self.assertRaises(ValueError, get_variations, "hello this is a test" )
        self.assertRaises(TypeError, get_variations, 1)




if __name__ == '__main__':
    unittest.main()