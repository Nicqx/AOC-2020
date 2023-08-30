import Days.Day1, Days.Day2, Days.Day3, Days.Day4
from Utility.read_to_array_int import read_to_array_int
from Utility.read_to_array_string import read_to_array_string
from Utility.read_to_array_string_w_d_enter import read_to_array_string_w_d_enter

arr = read_to_array_int("Days/Source/day1.txt")
print("Day1/1: " + str(Days.Day1.part1(arr)))
print("Day1/2: " + str(Days.Day1.part2(arr)))

arr = read_to_array_string("Days/Source/day2.txt")
print("Day2/1: " + str(Days.Day2.part1(arr)))
print("Day2/2: " + str(Days.Day2.part2(arr)))

arr = read_to_array_string("Days/Source/day3.txt")
print("Day3/1: " + str(Days.Day3.part1(arr)))
print("Day3/2: " + str(Days.Day3.part2(arr)))

arr = read_to_array_string_w_d_enter("Days/Source/day4.txt")
print("Day4/1: " + str(Days.Day4.part1(arr)))
print("Day4/2: " + str(Days.Day4.part2(arr)))
