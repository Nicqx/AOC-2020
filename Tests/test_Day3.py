from unittest import TestCase

from Days.Day3 import part1, part2
from Utility.read_to_array_string import read_to_array_string


class Test(TestCase):
    def test_part1(self):
        test_object = part1(read_to_array_string("Test_source/day3_test.txt"))
        expected_value = 7
        self.assertEqual(test_object, expected_value)

    def test_part2(self):
        test_object = part2(read_to_array_string("Test_source/day3_test.txt"))
        expected_value = 336
        self.assertEqual(test_object, expected_value)

    def test_main(self):
        test_object_part1 = part1(read_to_array_string("../Days/Source/day3.txt"))
        expected_value = 223
        self.assertEqual(test_object_part1, expected_value)

        test_object_part2 = part2(read_to_array_string("../Days/Source/day3.txt"))
        expected_value = 3517401300
        self.assertEqual(test_object_part2, expected_value)