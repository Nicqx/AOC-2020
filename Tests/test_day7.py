from unittest import TestCase

from Days.Day7 import part1,part2
from Utility.read_to_array_string import read_to_array_string


class Test(TestCase):
    def test_part1(self):
        test_object = part1(read_to_array_string("Test_source/day7_test1.txt"))
        expected_value = 4
        self.assertEqual(test_object, expected_value)

    def test_part2_1(self):
        test_object = part2(read_to_array_string("Test_source/day7_test1.txt"))
        expected_value = 32
        self.assertEqual(test_object, expected_value)

    def test_part2_2(self):
        test_object = part2(read_to_array_string("Test_source/day7_test2.txt"))
        expected_value = 126
        self.assertEqual(test_object, expected_value)

    def test_main(self):
        test_object_part1 = part1(read_to_array_string("../Days/Source/day7.txt"))
        expected_value = 332
        self.assertEqual(test_object_part1, expected_value)

        test_object_part2 = part2(read_to_array_string("../Days/Source/day7.txt"))
        expected_value = 10875
        self.assertEqual(test_object_part2, expected_value)
