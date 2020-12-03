def check_adjacent(code):
    last = -1
    for i in range(0, 6, 3):
        d0 = int(code[i])
        d1 = int(code[i + 1])
        d2 = int(code[i + 2])
        if d0 == d1 or d1 == d2 or d0 == last:
            return True
        last = d2
    return False


# 11 11 34 - example
def check_further_adjacent(code):
    # Check that adjacent digits doesn't appear more than two times
    last = None
    count = 0
    countofcount = 0
    i = 1
    while i < 6:
        d0 = int(code[i-1])
        d1 = int(code[i])
        if d0 == d1:
            count += 1
        else:
            if count > 0:
                countofcount += 1
            count = 0
        i += 1
    odd = countofcount + 1
    if count == 5:
        return True
    else:
        return not odd % 2 > 0


def check_increasing(code):
    # Convert to six ints
    d0 = int(code[0])
    d1 = int(code[1])
    d2 = int(code[2])
    d3 = int(code[3])
    d4 = int(code[4])
    d5 = int(code[5])
    return d5 >= d4 >= d3 >= d2 >= d1 >= d0


# Test codes
c1 = "111111"  # valid
c2 = "223450"  # invalid - decreasing (last)
c3 = "123789"  # invalid - no doubles
# Test for pt 2
c4 = '123444'  # invalid - adjacent 4's is big group"
c5 = '111122'  # valid - 11, 11, 22 - only double adjacent's
# 6 digit code in this sequence
seq = [171309, 643603]

test_codes = [int(c1), int(c2), int(c3), int(c4), int(c5)]
test_codes_2 = [112233, 123444, 111122]
if __name__ == "__main__":
    # check_further_adjacent('123444')
    for code in test_codes:
        a = check_adjacent(str(code))
        b = check_increasing(str(code))
        c = check_further_adjacent(str(code))

    print("run")
    # Fact: 6 digit code between seq[0] and seq[1]
    nr_possible_codes = seq[1] - seq[0]
    possibles = 0
    print("Number of codes: ", nr_possible_codes)
    # Fact: Two adjacent digits are the same
    for code in range(seq[0], seq[1]):
        # Check adjacent
        if not check_adjacent(str(code)):
            nr_possible_codes -= 1
            continue
        elif not check_increasing(str(code)):
            # Fact: Reading from left to right - each digit never decreases
            nr_possible_codes -= 1
            continue
        elif not check_further_adjacent(str(code)):
            # Fact (pt 2): If adjacent digits - they are not part of a bigger group
            nr_possible_codes -= 1
            continue
        else:
            # Possible code
            possibles += 1

    print("Number of possible codes: ", nr_possible_codes)
    print(possibles)
