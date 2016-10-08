# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

matrix = []

# Read in the rows and columns
rows, cols = raw_input().split(',')
rows = int(rows);   cols = int(cols)

# Calculate the total number of items
n = rows * cols

# Iterate through the row, convert to int, put in list
for row in xrange(rows):
    matrix.append([int(x) for x in raw_input().split(',')])

top = 0;    bottom = rows - 1
left = 0;   right = cols - 1
item = 1
side = 0

# As long as the pointers on each side do not cross each other
while top <= bottom and left <= right:

    # Top: Keep track of side so that it does not over print the matrix
    if side == 0:

        # In the top row, print all from the left to the right
        for i, val in enumerate(range(left, right + 1)):

            # If the item is the last in the matrix, do not print a comma
            if item == n:
                sys.stdout.write(str(matrix[top][val]))
            else:
                sys.stdout.write(str(matrix[top][val]) + ",")
                item += 1
        top += 1

    # Right
    if side == 1:
        for val in range(top, bottom + 1):
            if item == n:
                sys.stdout.write(str(matrix[val][right]))
            else:
                sys.stdout.write(str(matrix[val][right]) + ",")
                item += 1
        right -= 1

    # Bottom
    if side == 2:
        for val in reversed(range(left, right + 1)):
            if item == n:
                sys.stdout.write(str(matrix[bottom][val]))
            else:
                sys.stdout.write(str(matrix[bottom][val]) + ",")
                item += 1
        bottom -= 1

    # Left
    if side == 3:
        for i, val in enumerate(reversed(range(top, bottom + 1))):
            if item == n:
                sys.stdout.write(str(matrix[val][right]))
            else:
                sys.stdout.write(str(matrix[val][left]) + ",")
                item += 1
        left += 1

    # Iterate the side, then mod 4 to keep it within 0 - 3
    side += 1
    side %= 4




