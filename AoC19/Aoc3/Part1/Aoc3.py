import numpy as np


def add_wire(direction, length):
    return 0


def calculate_end_pos(move, past_position):
    direction = move[0]
    length = int(move[1:])
    new_pos = past_position[:]
    if direction == "R":
        # Increment x
        new_pos[0] += length
    elif direction == "U":
        # Increment y
        new_pos[1] += length
    elif direction == "L":
        # Decrease x
        new_pos[0] -= length
    elif direction == "D":
        # Decrease y
        new_pos[1] -= length

    return new_pos


def get_move_vec(start, end):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    step = 1
    if x2 != x1:
        if x2 < x1:
            step = -1
        xvec = np.arange(x1, x2 + 1 * sign(step), step)
        yvec = np.ones_like(xvec) * y1
    else:
        if y2 < y1:
            step = -1
        yvec = np.arange(y1, y2 + 1 * sign(step), step)
        xvec = np.ones_like(yvec) * x1

    return xvec, yvec


def sign(q):
    if q >= 0:
        return 1
    else:
        return -1


if __name__ == "__main__":
    # w1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    # w2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    # ans 135
    # w1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    # w2 = "U62,R66,U55,R34,D71,R55,D58,R83"
    # ans 159
    # w1 = "R8,U5,L5,D3"
    # w2 = "U7,R6,D4,L4"
    # ans 6

    f = open("Data/3_w1.txt", "r")
    w1 = f.readline()
    w1 = list(w1.split(","))
    f.close()
    f = open("Aoc3/Data/3_w2.txt", "r")
    w2 = f.readline()
    w2 = list(w2.split(","))

    # Index slicing for wired path
    # Wire one start at (0, 0)
    # First move - R8
    # => Wire from (0, 0) to (8, 0)
    # Second move - U5
    # => wire from (8, 0) to (8, 5)
    # Third move - L5
    # => wire from (8, 5) to (3, 5) [85 75 65 55 45 34]
    # Fourth move - D3
    # => wire from (3, 5) to (3, 2) [35 34 33 32]

    # Wire two start at (0, 0)
    # First move - U7
    # => wire from (0, 0) to (0, 7)
    # Second move - R6
    # => wire from (0, 7) to (6, 7)
    # Third move - D4
    # => wire from (6, 7) to (6, 3) [67 66 65 64 63]
    # Fourth move - L4
    # => wire from (6, 3) to (2, 3) [63 53 43 33 23]

    # Crossings at (6, 5) AND (3, 3)

    # Wire end at (x,y)
    initial_pos = [0, 0]
    x_coords1 = []
    y_coords1 = []
    x_coords2 = []
    y_coords2 = []
    cross_vec = []

    for moves in w1:
        # Calculate wire end points after move
        move_end = calculate_end_pos(moves, initial_pos)
        # Get vector of path
        xmov, ymov = get_move_vec(initial_pos, move_end)
        x_coords1.append(xmov)
        y_coords1.append(ymov)
        # Update end point pos for next move!
        initial_pos = move_end

    initial_pos = [0, 0]  # For wire two
    for mvs in w2:
        mend = calculate_end_pos(mvs, initial_pos)
        xmov, ymov = get_move_vec(initial_pos, mend)
        x_coords2.append(xmov)
        y_coords2.append(ymov)
        initial_pos = mend

    # Find intersection of wire elements
    # Count the wire elements
    n_elements = [len(x_coords1), len(x_coords2)]
    # Select the one with fewest elements
    n = min(n_elements)

    for j in range(len(x_coords1)):
        # Select one x,y path for one wire (wire one)
        w1x = x_coords1[j]
        w1y = y_coords1[j]
        # And compare this path to all other path of wire two
        for path in range(len(y_coords2)):
            testx = np.isin(w1x, x_coords2[path])
            testy = np.isin(w1y, y_coords2[path])
            crossing = testx & testy
            if True in crossing:
                cross_coord = [w1x[crossing][0], w1y[crossing][0]]
                cross_vec.append(cross_coord)

    cross_vec.remove([0, 0])
    print(cross_vec)
    manhattans = []
    for elem in cross_vec:
        manhattans.append(abs(elem[0]) + abs(elem[1]))
    print(manhattans)
    print(min(manhattans))
