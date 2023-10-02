from unittest import TestCase

from Days.Day8 import part1, part2
from Utility.read_to_array_string import read_to_array_string


class Test(TestCase):
    def test_part1(self):
        test_object = part1(read_to_array_string("Test_source/day8_test.txt"))
        expected_value = 5
        self.assertEqual(test_object, expected_value)

    def test_part2(self):
        test_object = part2(read_to_array_string("Test_source/day8_test.txt"))
        expected_value = 8
        self.assertEqual(test_object, expected_value)

    def test_main(self):
        test_object_part1 = part1(read_to_array_string("../Days/Source/day8.txt"))
        expected_value = 1816
        self.assertEqual(test_object_part1, expected_value)

        test_object_part2 = part2(read_to_array_string("../Days/Source/day8.txt"))
        expected_value = 1149
        self.assertEqual(test_object_part2, expected_value)
