def part1(local_array):
    x = 0
    y = 0
    hossz = len(local_array[0])
    counter = 0

    # jobbra 3 le 1
    while y < len(local_array):
        if (local_array[y][x] == "#"):
            counter += 1
        x += 3
        y += 1
        if x >= hossz:
            x -= hossz

    return counter

def part2(local_array):
    pattern = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    hossz = len(local_array[0])
    counter = 1
    for round in pattern:
        local_counter = 0
        x = 0
        y = 0
        while y < len(local_array):
            if (local_array[y][x] == "#"):
                local_counter += 1
            x += round[0]
            y += round[1]
            if x >= hossz:
                x -= hossz
        counter *= local_counter
    return counter