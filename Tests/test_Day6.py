from unittest import TestCase

from Days.Day6 import part1, part2
from Utility.read_to_array_string_w_d_enter import read_to_array_string_w_d_enter


class Test(TestCase):
    def test_part1(self):
        test_object = part1(read_to_array_string_w_d_enter("Test_source/day6_test_1_1.txt"))
        expected_value = 6
        self.assertEqual(test_object, expected_value)
        test_object = part1(read_to_array_string_w_d_enter("Test_source/day6_test_1_2.txt"))
        expected_value = 11
        self.assertEqual(test_object, expected_value)

    def test_part2(self):
        test_object = part2(read_to_array_string_w_d_enter("Test_source/day6_test_1_2.txt"))
        expected_value = 6
        self.assertEqual(test_object, expected_value)

    def test_main(self):
        test_object_part1 = part1(read_to_array_string_w_d_enter("../Days/Source/day6.txt"))
        expected_value = 6161
        self.assertEqual(test_object_part1, expected_value)

        test_object_part2 = part2(read_to_array_string_w_d_enter("../Days/Source/day6.txt"))
        expected_value = 2971
        self.assertEqual(test_object_part2, expected_value)
