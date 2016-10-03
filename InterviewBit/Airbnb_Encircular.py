'''
# Complete the function below.


def  doesCircleExist(commands):

    # Iterate through list of command strings
    for i, command in enumerate(commands):

        # Position stored as pair of x and y
        position = (0, 0)

        # Direction facing is stored as 0: North, 1: East, 2: South, 3: West
        facing = 0


        # Iterate through this command string four times total, first three below
        for iterate in xrange(3):
            for j, instruction in enumerate(command):

                position, facing = myCompass(instruction, position, facing)

        # Final iteration, four times because direction can change four times
        for j, instruction in enumerate(command):

            position, facing = myCompass(instruction, position, facing)

            # If the last element of the current string of commands
            if j == len(command) - 1:

                # If the position and direction is the same as the starting configuration:
                if position == (0, 0) and facing == 0:
                    # Assign command string in list to YES
                    commands[i] = "YES"
                else:
                    # Assign command string in list to NO
                    commands[i] = "NO"

    return commands


def myCompass(move, position, facing):

    x, y = position

    if move == 'L':
        if facing == 0:
            facing = 3
        else:
            facing -= 1

    if move == 'R':
        if facing == 3:
            facing = 0
        else:
            facing += 1

    if move == 'G':
        if facing == 0:
            y += 1
        if facing == 1:
            x += 1
        if facing == 2:
            y -= 1
        if facing == 3:
            x -= 1

    position = (x, y)
    return position, facing
'''

def doesCircleExist(commands):

    # Iterate through list of command strings
    for i, command in enumerate(commands):

        # Position stored as pair of x and y
        position = (0, 0)

        # Direction facing is stored as 0: North, 1: East, 2: South, 3: West
        facing = 0

        # Iterate through this command string four times total, first three below
        for iterate in xrange(3):
            for j, instruction in enumerate(command):
                position, facing = myCompass(instruction, position, facing)

        # Final iteration, four times because direction can change four times
        for j, instruction in enumerate(command):

            position, facing = myCompass(instruction, position, facing)

            # If the last element of the current string of commands
            if j == len(command) - 1:

                # If the position and direction is the same as the starting configuration:
                if position == (0, 0) and facing == 0:
                    # Assign command string in list to YES
                    commands[i] = "YES"
                else:
                    # Assign command string in list to NO
                    commands[i] = "NO"

    return commands


def myCompass(move, position, facing):

    x, y = position

    if move == 'L':
        if facing == 0:
            facing = 3
        else:
            facing -= 1

    if move == 'R':
        if facing == 3:
            facing = 0
        else:
            facing += 1

    if move == 'G':
        if facing == 0:
            y += 1
        if facing == 1:
            x += 1
        if facing == 2:
            y -= 1
        if facing == 3:
            x -= 1

    position = (x, y)
    return position, facing

