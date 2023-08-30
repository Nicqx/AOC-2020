from unittest import TestCase

from Utility.read_to_array_int import read_to_array_int
from Utility.read_to_array_string import read_to_array_string
from Utility.read_to_array_string_w_d_enter import read_to_array_string_w_d_enter


class Test(TestCase):
    def test_read_to_array_int(self):
        test_object = read_to_array_int("Test_source/int_array_test.txt")
        self.assertTrue(isinstance(test_object, list))
        self.assertIsInstance(test_object, list)
        self.assertEqual(len(test_object), 3)
        self.assertEqual(test_object, [1, 2, 3])

    def test_read_to_array_string(self):
        test_object = read_to_array_string("Test_source/string_array_test.txt")
        self.assertTrue(isinstance(test_object, list))
        self.assertIsInstance(test_object, list)
        self.assertEqual(len(test_object), 3)
        self.assertEqual(test_object, ['alma', 'korte', 'dragonfruit'])

    def test_read_to_array_string_w_d_enter(self):
        test_object = read_to_array_string_w_d_enter("Test_source/string_w_d_enter_array_test.txt")
        self.assertTrue(isinstance(test_object, list))
        self.assertIsInstance(test_object, list)
        self.assertEqual(len(test_object), 3)
        self.assertEqual(test_object, ['egy:1', 'ketto:2 harom:3', 'negy:alma'])
