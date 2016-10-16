def selection_sort(a_list):

    if not a_list:
        return None

    for i in xrange(len(a_list)-1):

        current_min = a_list[i]
        min_index = i

        for j in xrange(i+1, len(a_list)):

            if a_list[j] < current_min:

                current_min = a_list[j]
                min_index = j

        a_list[i], a_list[min_index] = a_list[min_index], a_list[i]

    return a_list

a_list = [2, 6, 8, 3, 6, 1, 1, 12]
print selection_sort(a_list)