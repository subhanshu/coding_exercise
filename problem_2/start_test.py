import unittest
from start import rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8
from rectangle import Rectangle

class testRectangles(unittest.TestCase):
    def test_rect(self):
        #test for object creation
        self.assertIsInstance(Rectangle(10,10,20,20), Rectangle)
        #test for type errors
        self.assertRaises(TypeError, Rectangle, "a",10,20,20)
        self.assertRaises(TypeError, Rectangle, "10","10","20","20")

    def test_covered(self):
        self.assertEqual(rect1.is_covered(rect2), "COVERED")
        self.assertEqual(rect1.is_covered(rect3), "COVERED")
        self.assertEqual(rect1.is_covered(rect7), "PARTIALLY_COVERED")
        self.assertEqual(rect1.is_covered(rect8), "PARTIALLY_COVERED")
        self.assertEqual(rect1.is_covered(rect4), False)
        self.assertEqual(rect1.is_covered(rect5), False)
        self.assertRaises(TypeError, rect1.is_covered,"22")