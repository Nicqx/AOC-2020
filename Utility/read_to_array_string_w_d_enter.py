def read_to_array_string_w_d_enter(file):
    array = []
    fo = open(file, "r")
    whole_file = fo.read()
    whole_file = whole_file.replace("\n\n", "@")
    whole_file = whole_file.replace("\n", " ")
    whole_file = whole_file.replace("@", "\n")
    for line in whole_file.split("\n"):
        array.append(line)

    fo.close()
    return array
