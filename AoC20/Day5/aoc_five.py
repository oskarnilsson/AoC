import numpy as np
# Binary toggling bits
# For rows: 'F' - "de"-set bit (i.e make it zero)
#           'B' - set bit (i.e make it one)
# For columns: 'L' - "de"-set bit (i.e make it zero)
#              'R' - set bit (i.e make it one)
# Seat ID : 8*row + column

# Ans to test:
# row 70, col 7, ID 567
# row 14, col 7, ID 119
# row 102, col 4, ID 820

# Part one: Find the highest seat ID
# Part two: Find a missing seat ID

def map_string_to_bin(str):
    binary_str = '0b'
    for i, char in enumerate(str):
        if char == 'F' or char == 'L':
            binary_str += '0'
        elif char == 'B' or char == 'R':
            binary_str += '1'
        # else
        # do nothing, escape character here
    return binary_str



if __name__ == "__main__":
    seat_id = []
    f = open("day5.txt", "r")
    for lines in f:
        to_row = map_string_to_bin(lines[0:7])
        to_col = map_string_to_bin(lines[7:])
        row = int(to_row, 2)
        col = int(to_col, 2)
        seat_id.append(8*row + col)
    print(seat_id)
    print(max(seat_id))
    # Sort the seat ID's
    sorted = np.sort(seat_id)
    last = sorted[0]
    for id in sorted:
        if id - last > 1:
            print(id - 1)
        last = id
