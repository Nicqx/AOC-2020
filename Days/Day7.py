import re


def part1(arr_local):
    arr_local = list(map(lambda st: str.replace(st, "bags", "bag"), arr_local))
    arr_local = list(map(lambda st: str.replace(st, " bag", ""), arr_local))
    arr_local = list(map(lambda st: str.replace(st, ".", ""), arr_local))
    bag_list = {}
    for item in arr_local:
        mo = re.match(r'(\w*\W\w*)\Wcontain\W(.*)', item)
        bag_list[mo.group(1)] = mo.group(2)

    counter = 0
    for bag in bag_list.keys():
        if check_a_bag_content_shiny_gold(bag_list[bag], bag_list):
            counter += 1

    return counter


def part2(arr_local):
    arr_local = list(map(lambda st: str.replace(st, "bags", "bag"), arr_local))
    arr_local = list(map(lambda st: str.replace(st, " bag", ""), arr_local))
    arr_local = list(map(lambda st: str.replace(st, ".", ""), arr_local))
    bag_list = {}
    for item in arr_local:
        mo = re.match(r'(\w*\W\w*)\Wcontain\W(.*)', item)
        bag_list[mo.group(1)] = mo.group(2)

    starter_bag = "shiny gold"

    return extract_bag(starter_bag, bag_list)


def extract_bag(starter, bags):
    if bags[starter] == "no other":
        return 0
    else:
        counter = 0
        content = bags[starter].split(", ")
        for item in content:
            mo = re.match(r'(\d+)\W(.+)', item)
            counter += (int(mo.group(1)) + int(mo.group(1)) * extract_bag(mo.group(2), bags))
        return counter


def check_a_bag_content_shiny_gold(contents, bags):
    content = contents.split(", ")
    for item in content:
        mo = re.match(r'(\d+)\W(.+)', item)
        if mo:
            if mo.group(2) == "shiny gold":
                return True
            else:
                if check_a_bag_content_shiny_gold(bags[mo.group(2)], bags):
                    return True

    return False
