from unittest import TestCase

from Utility.read_to_array_int import read_to_array_int
from Utility.read_to_array_string import read_to_array_string


class Test(TestCase):
    def test_read_to_array_int(self):
        test_object = read_to_array_int("Test_source/day1_test.txt")
        self.assertTrue(isinstance(test_object, list))
        self.assertIsInstance(test_object, list)
        self.assertEqual(len(test_object), 6)
        self.assertEqual(test_object, [1721, 979, 366, 299, 675, 1456])

    def test_read_to_array_string(self):
        test_object = read_to_array_string("Test_source/day2_test.txt")
        self.assertTrue(isinstance(test_object, list))
        self.assertIsInstance(test_object, list)
        self.assertEqual(len(test_object), 3)
        self.assertEqual(test_object, ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"])