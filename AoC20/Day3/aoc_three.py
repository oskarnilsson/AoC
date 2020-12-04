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


# [...8] + 3 -> 9, 10(MAX),0
# 10 - 8 = 2

# 9 + 3 -> 10(MAX), 0, 1
def get_next_column(last, step=3):
    # If last + step will
    if last == MAX_COL_INDEX:
        return step - 1
    elif last + step > MAX_COL_INDEX:
        return (last + step) - MAX_COL_INDEX - 1
    else:
        return last + step


# Count trees following path right 3 - down 1
if __name__ == "__main__":
    # Read input
    f = open("day3.txt", "r")
    sled_map = f.read().split('\n')

    #  For test input:
    # sled_map = dummy_map
    MAX_COL_INDEX = len(sled_map[0]) - 1

    step_size = [1, 3, 5, 7, 1]
    step_down_size = [1, 1, 1, 1, 2]
    trees_on_path = []

    for i, step in enumerate(step_size):
        # For every step :
        number_of_open_visited = 0
        number_of_trees_visited = 0
        col = 0
        row_step = step_down_size[i]
        for j in range(0, len(sled_map), row_step):
            # print(row)
            # Go to correct column
            what_have_we_here = sled_map[j][col]
            col = get_next_column(col, step=step)
            if what_have_we_here == '#':
                number_of_trees_visited += 1
            elif what_have_we_here == '.':
                number_of_open_visited += 1
            else:
                print("SOMETHING IS WRONG HERE!")

        trees_on_path.append(number_of_trees_visited)

    print("Number of trees visited: {}".format(trees_on_path))
    mul = 1
    for num in trees_on_path:
        mul *= num

    print(mul)
