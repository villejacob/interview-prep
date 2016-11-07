number = 19

# soln = []
# while number > 10:
#     soln.append(number%10)
#     number /= 10
# soln.append(number)
#
# soln = [val**2 for val in soln]
#
# for val in soln:
#     number += val
#
# print number
#
# print soln

visited = set([])

while number != 1:
    number_list = []
    while number >= 10:
        number_list.append(number % 10)
        number /= 10
    number_list.append(number)

    number_list = [val ** 2 for val in number_list]

    number = 0

    for val in number_list:
        number += val

    if number in visited:
        print False
    else:
        visited.add(number)
print True