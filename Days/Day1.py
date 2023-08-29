def part1(arr_local):
    x = 0
    y = 0
    found = False

    while x < len(arr_local) and not found:
        y = x
        while y < len(arr_local) and not found:
            found = arr_local[x] + arr_local[y] == 2020
            y += 1
        x += 1

    return arr_local[x - 1] * arr_local[y - 1]


def part2(arr_local):
    x = 0
    y = 0
    z = 0
    found = False

    while x < len(arr_local) and not found:
        y = x
        while y < len(arr_local) and not found:
            z = y
            while z < len(arr_local) and not found:
                found = arr_local[x] + arr_local[y] + arr_local[z] == 2020
                z += 1
            y += 1
        x += 1
    return arr_local[x - 1] * arr_local[y - 1] * arr_local[z - 1]
