import Days.Day1, Days.Day2
from Utility.read_to_array_int import read_to_array_int
from Utility.read_to_array_string import read_to_array_string

arr = read_to_array_int("Days/Source/day1.txt")
print("Day1/1: " + str(Days.Day1.part1(arr)))
print("Day1/2: " + str(Days.Day1.part2(arr)))

arr = read_to_array_string("Days/Source/day2.txt")
print("Day2/1: " + str(Days.Day2.part1(arr)))
print("Day2/2: " + str(Days.Day2.part2(arr)))