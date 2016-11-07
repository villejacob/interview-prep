def find_partitions(input_list):

    output = []

    first = input_list[0]
    last = input_list[0]

    # i increments one below the current value in the input
    i = 0

    for val in input_list[1:]:
        # Current is the last incremented by one
        if input_list[i] + 1 == val:
            last = val
        else:
            if first != last:
                output_string = str(first) + '-' + str(last)
                output.append(output_string)
            else:
                output.append(last)
            first = val
            last = val

        i += 1

    if first == last:
        output.append(last)
    else:
        output_string = str(first) + '-' + str(last)
        output.append(output_string)

    return output




input_list = [1, 2, 3, 5, 7, 8, 9, 11]
print find_partitions(input_list)
