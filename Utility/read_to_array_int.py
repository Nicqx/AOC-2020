def read_to_array_int(file):
    array = []
    fo = open(file, "r")
    line = fo.readline()
    while line:
        if line[len(line) - 1] == '\n':
            line = line[:-1]
        array.append(int(line))
        line = fo.readline()

    fo.close()
    return array
