import re


def part1(arr_local):
    counter = 0
    for element in arr_local:
        mo = re.match(r"(\d+)-(\d+)\W(\w):\W(\w+)", element)
        if mo and (int(mo.group(1)) <= mo.group(4).count(mo.group(3)) <= int(mo.group(2))):
            counter += 1

    return counter


def part2(arr_local):
    counter = 0
    for element in arr_local:
        mo = re.match(r"(\d+)-(\d+)\W(\w):\W(\w+)", element)
        if mo and ((mo.group(4)[int(mo.group(1)) - 1] == mo.group(3)) ^ (
                mo.group(4)[int(mo.group(2)) - 1] == mo.group(3))):
            counter += 1

    return counter
