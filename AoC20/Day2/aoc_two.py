

count_valid = 0
if __name__ == '__main__':
    f = open("day2.txt", "r")
    for lines in f:
        splits = lines.split()
        repetitions_str = splits[0].split('-')
        repetitions = [int(repetitions_str[0]), int(repetitions_str[1])]
        character = splits[1][0]
        password = splits[2]
        number = password.count(character)
        if repetitions[0] <= number <= repetitions[1]:
            count_valid += 1
    print("Number of valid passwords: {}".format(count_valid))
    f.close()

    count_valid = 0
    # Part 2
    f = open("day2.txt", "r")
    for lines in f:
        splits = lines.split()
        repetitions_str = splits[0].split('-')
        indices = [int(repetitions_str[0]), int(repetitions_str[1])]
        character = splits[1][0]
        password = splits[2]
        # Check that character is present at either first or second index
        first = password[indices[0]-1] == character
        second = password[indices[1]-1] == character
        if first ^ second:  # ^ - xor, since we have to check first and not second, or second and not first
            count_valid += 1

    f.close()
    print("Valid passwords according to new rule: {}".format(count_valid))