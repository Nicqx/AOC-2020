def part1(arr_local):
    array_of_set = []
    counter = 0
    for element in arr_local:
        s = set()
        for letter in element:
            if letter == ' ':
                continue
            s.add(letter)
        array_of_set.append(s)
    for element in array_of_set:
        counter += len(element)

    return counter


def part2(arr_local):
    counter = 0
    for element in arr_local:
        persons = 1
        d = {}
        for letter in element:
            if letter == ' ':
                persons += 1
                continue
            if letter not in d.keys():
                d[letter] = 1
            else:
                d[letter] += 1
        for key in d.keys():
            if d[key] == persons:
                counter += 1

    return counter
