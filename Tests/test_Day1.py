from unittest import TestCase

from Days.Day1 import part2, part1
from Utility.read_to_array_int import read_to_array_int


class Test(TestCase):
    def test_part1(self):
        test_object = part1(read_to_array_int("Test_source/day1_test.txt"))
        expected_value = 514579
        self.assertEqual(test_object, expected_value)

    def test_part2(self):
        test_object = part2(read_to_array_int("Test_source/day1_test.txt"))
        expected_value = 241861950
        self.assertEqual(test_object, expected_value)

    def test_main(self):
        test_object_part1 = part1(read_to_array_int("../Days/Source/day1.txt"))
        expected_value = 633216
        self.assertEqual(test_object_part1, expected_value)

        test_object_part2 = part2(read_to_array_int("../Days/Source/day1.txt"))
        expected_value = 68348924
        self.assertEqual(test_object_part2, expected_value)

