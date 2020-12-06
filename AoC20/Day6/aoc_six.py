
ans_sheet = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0,
        'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
        'w': 0, 'x': 0, 'y': 0, 'z': 0
    }

if __name__ == "__main__":
    group_ans = []
    ans = ans_sheet.copy()

    f = open("day6.txt", "r")
    for line in f:
        if line == "\n":
            print("New group:")
            group_ans.append(ans)
            ans = dict(ans_sheet)
        else:
            print(line)
            for char in line:
                if char != '\n':
                    ans[char] = 1

    group_ans.append(ans)

    print("Parse done")
    count_yes = 0
    for sheet in group_ans:

        for key in sheet:
            if sheet[key] == 0:
                continue
            count_yes += sheet[key]
    print(count_yes)
    print("Number of groups: {}".format(len(group_ans)))
