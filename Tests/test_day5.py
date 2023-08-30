from unittest import TestCase

from Days.Day5 import part1, part2
from Utility.read_to_array_string import read_to_array_string


class Test(TestCase):
    def test_part1(self):
        test_object = part1(read_to_array_string("Test_source/day5_test_1.txt"))
        expected_value = 357
        self.assertEqual(test_object, expected_value)
        test_object = part1(read_to_array_string("Test_source/day5_test_2.txt"))
        expected_value = 567
        self.assertEqual(test_object, expected_value)
        test_object = part1(read_to_array_string("Test_source/day5_test_3.txt"))
        expected_value = 119
        self.assertEqual(test_object, expected_value)
        test_object = part1(read_to_array_string("Test_source/day5_test_4.txt"))
        expected_value = 820
        self.assertEqual(test_object, expected_value)

    def test_main(self):
        test_object_part1 = part1(read_to_array_string("../Days/Source/day5.txt"))
        expected_value = 951
        self.assertEqual(test_object_part1, expected_value)

        test_object_part2 = part2(read_to_array_string("../Days/Source/day5.txt"))
        expected_value = 653
        self.assertEqual(test_object_part2, expected_value)