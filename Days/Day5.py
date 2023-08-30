def part1(arr_local):
    max_id = 0
    for element in arr_local:
        local_row_low = 0
        local_row_high = 127
        local_column_low = 0
        local_column_high = 7
        if element[0] == 'F':
            local_row_high = local_row_high - int((local_row_high - local_row_low) / 2) - 1
        else:
            local_row_low = local_row_low + int((local_row_high - local_row_low) / 2) + 1
        if element[1] == 'F':
            local_row_high = local_row_high - int((local_row_high - local_row_low) / 2) - 1
        else:
            local_row_low = local_row_low + int((local_row_high - local_row_low) / 2) + 1
        if element[2] == 'F':
            local_row_high = local_row_high - int((local_row_high - local_row_low) / 2) - 1
        else:
            local_row_low = local_row_low + int((local_row_high - local_row_low) / 2) + 1
        if element[3] == 'F':
            local_row_high = local_row_high - int((local_row_high - local_row_low) / 2) - 1
        else:
            local_row_low = local_row_low + int((local_row_high - local_row_low) / 2) + 1
        if element[4] == 'F':
            local_row_high = local_row_high - int((local_row_high - local_row_low) / 2) - 1
        else:
            local_row_low = local_row_low + int((local_row_high - local_row_low) / 2) + 1
        if element[5] == 'F':
            local_row_high = local_row_high - int((local_row_high - local_row_low) / 2) - 1
        else:
            local_row_low = local_row_low + int((local_row_high - local_row_low) / 2) + 1
        if element[6] == 'F':
            selected_row = local_row_low
        else:
            selected_row = local_row_high

        if element[7] == 'R':
            local_column_low = local_column_low + int((local_column_high - local_column_low) / 2) + 1
        else:
            local_column_high = local_column_high - int((local_column_high - local_column_low) / 2) - 1
        if element[8] == 'R':
            local_column_low = local_column_low + int((local_column_high - local_column_low) / 2) + 1
        else:
            local_column_high = local_column_high - int((local_column_high - local_column_low) / 2) - 1
        if element[9] == 'R':
            selected_column = local_column_high
        else:
            selected_column = local_column_low

        max_id = max(selected_row * 8 + selected_column, max_id)
    return max_id


def part2(arr_local):
    full_list = set()
    for i in range(128):
        for j in range(8):
            full_list.add(i * 8 + j)

    max_id = 0
    for element in arr_local:
        local_row_low = 0
        local_row_high = 127
        local_column_low = 0
        local_column_high = 7
        if element[0] == 'F':
            local_row_high = local_row_high - int((local_row_high - local_row_low) / 2) - 1
        else:
            local_row_low = local_row_low + int((local_row_high - local_row_low) / 2) + 1
        if element[1] == 'F':
            local_row_high = local_row_high - int((local_row_high - local_row_low) / 2) - 1
        else:
            local_row_low = local_row_low + int((local_row_high - local_row_low) / 2) + 1
        if element[2] == 'F':
            local_row_high = local_row_high - int((local_row_high - local_row_low) / 2) - 1
        else:
            local_row_low = local_row_low + int((local_row_high - local_row_low) / 2) + 1
        if element[3] == 'F':
            local_row_high = local_row_high - int((local_row_high - local_row_low) / 2) - 1
        else:
            local_row_low = local_row_low + int((local_row_high - local_row_low) / 2) + 1
        if element[4] == 'F':
            local_row_high = local_row_high - int((local_row_high - local_row_low) / 2) - 1
        else:
            local_row_low = local_row_low + int((local_row_high - local_row_low) / 2) + 1
        if element[5] == 'F':
            local_row_high = local_row_high - int((local_row_high - local_row_low) / 2) - 1
        else:
            local_row_low = local_row_low + int((local_row_high - local_row_low) / 2) + 1
        if element[6] == 'F':
            selected_row = local_row_low
        else:
            selected_row = local_row_high

        if element[7] == 'R':
            local_column_low = local_column_low + int((local_column_high - local_column_low) / 2) + 1
        else:
            local_column_high = local_column_high - int((local_column_high - local_column_low) / 2) - 1
        if element[8] == 'R':
            local_column_low = local_column_low + int((local_column_high - local_column_low) / 2) + 1
        else:
            local_column_high = local_column_high - int((local_column_high - local_column_low) / 2) - 1
        if element[9] == 'R':
            selected_column = local_column_high
        else:
            selected_column = local_column_low

        full_list.remove(selected_row * 8 + selected_column)
        max_id = max(selected_row * 8 + selected_column, max_id)
    for i in range(max_id + 1, max(full_list) + 1):
        full_list.remove(i)
    return max(full_list)
