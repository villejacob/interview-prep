def excel_column_number_to_name(column_number):
    # Approach: Convert the same way binary is converted to decimal
    # Divide the number by the base (26 because of the alphabet)
    # Get the number from the remainder (Using ascii characters, A starts at 65)

    name = ""

    # Continue until the length of the alphabet no longer "fits" in the number
    while column_number > 0:
        # Perform quotient and remainder operations
        column_number, remainder = divmod(column_number, 26)
        # Edge case when remainder is 0, append Z
        if remainder == 0:
            name += 'Z'
            # Decrement column number because a value is taken away as 'Z'
            column_number -= 1
        else:
            # Add the character to the output
            name += chr(remainder + 64)

    # return output in reverse, because it is calculated from lsb to msb
    return name[::-1]

print excel_column_number_to_name(32)