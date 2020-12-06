# ans_sheet = {
#        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0,
#        'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
#        'w': 0, 'x': 0, 'y': 0, 'z': 0
#    }

if __name__ == "__main__":
    group_ans = []

    ans = {"Persons_in_group": 0}
    count_group_members = 0
    f = open("day6.txt", "r")
    for line in f:
        if line == "\n":
            print("New group:")
            ans["Persons_in_group"] = count_group_members
            group_ans.append(ans)

            ans = {}
            count_group_members = 0
        else:
            count_group_members += 1
            print(line)
            for char in line:
                if char != '\n':
                    if char in ans:
                        ans[char] = ans[char] + 1
                    else:
                        ans[char] = 1

    group_ans.append(ans)
    ans["Persons_in_group"] = count_group_members
    print("Parse done")
    count_yes = 0
    count_all_yes = 0
    for sheet in group_ans:
        people_in_group = sheet.pop("Persons_in_group", None)
        count_yes += len(sheet)  # Total number of questions answered with "yes"
        for key in sheet:
            # If all people in group answered with yes
            # ans[sheet]/people_in_group = 1
            if sheet[key] / people_in_group == 1:
                count_all_yes += 1

    print(count_yes)
    print("Number of groups: {}".format(len(group_ans)))
    print("Sum of number of questions answered yes by everyone: {}".format(count_all_yes))
