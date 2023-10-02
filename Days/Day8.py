import re


def part1(arr_local):
    return run_code(arr_local)[1]


def part2(arr_local):
    for element in range(len(arr_local)):
        new_arr = clone_arr(arr_local, element)
        result = run_code(new_arr)
        if result[0]:
            return result[1]


def clone_arr(arr, poz):
    arr_new = []
    for i in range(len(arr)):
        if i == poz:
            if arr[i][:3] == "nop":
                tmp = arr[i]
                tmp = tmp.replace("nop", "jmp")
                arr_new.append(tmp)
            else:
                tmp = arr[i]
                tmp = tmp.replace("jmp", "nop")
                arr_new.append(tmp)
        else:
            arr_new.append(arr[i])
    return arr_new


def run_code(arr_local):
    result = [False, 0]
    ac = 0
    poz = 0
    used_instruction = set()
    while True:
        if poz in used_instruction:
            break
        if poz == len(arr_local):
            result[0] = True
            break
        used_instruction.add(poz)
        mo = re.search(r'(\w{3})\W((\+|-)\d+)', arr_local[poz])
        if mo.group(1) == "nop":
            poz += 1
            continue
        if mo.group(1) == "acc":
            if mo.group(3) == "+":
                ac += int(mo.group(2)[1:])
            else:
                ac -= int(mo.group(2)[1:])
            poz += 1
            continue
        if mo.group(1) == "jmp":
            if mo.group(3) == "+":
                poz += int(mo.group(2)[1:])
            else:
                poz -= int(mo.group(2)[1:])
    result[1] = ac
    return result
