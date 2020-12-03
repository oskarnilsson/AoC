# https://adventofcode.com/2020/day/3

# . (dot) - open space
# # (pound) - a tree
# Test input
dummy_map = [
    '..##.......',
    '#...#...#..',
    '.#....#..#.',
    '..#.#...#.#',
    '.#...##..#.',
    '..#.##.....',
    '.#.#.#....#',
    '.#........#',
    '#.##...#...',
    '#...##....#',
    '.#..#...#.#'
]

MAX_COL_INDEX = len(dummy_map[0]) - 1


# [...8] + 3 -> 9, 10(MAX),0 <- ANS
def get_next_column(last, step=3):
    # If last + step will
    if last == MAX_COL_INDEX:
        return step - 1
    elif last + step > MAX_COL_INDEX:
        new_col = MAX_COL_INDEX - last
        # last = 0
        return new_col
    else:
        return last + step


number_of_open_visited = 0
number_of_trees_visited = 0
# Count trees following path right 3 - down 1
if __name__ == "__main__":
    start_row = 0  # Increase by one every run
    start_col = 0  # Increase by three every run
    print(dummy_map[start_row])
    # For every step :
    col = 0
    for i, row in enumerate(dummy_map):
        # print(row)
        # Go to correct column
        what_have_we_here = row[col]
        col = get_next_column(col, step=3)
        if what_have_we_here == '#':
            number_of_trees_visited += 1
        elif what_have_we_here == '.':
            number_of_open_visited += 1
        else:
            print("SOMETHING IS WRONG HERE!")
        # print(row[:col] + 'X' + row[col+1:])

    print("Number of trees visited: {}".format(number_of_trees_visited))
