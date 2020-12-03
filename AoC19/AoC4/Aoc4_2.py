import numpy as np


def check_adjacent_groups(code):
    d0 = int(code[0])
    rep = 0
    repv = []
    for i in range(1, 6):
        d = int(code[i])
        if d == d0:
            rep += 1
        else:
            if rep != 0:
                repv.append(rep)
                rep = 0
        d0 = d
    repv.append(rep) # 177778
    maxr = max(repv) # 3, 0
    if sum(repv) >= 1: # Repeating digits identified
        if maxr % 2 == 0 and sum(repv) == maxr: # Even max means 3 or 5 digit repetition
            return False  # Code is invalid
        elif maxr % 2 > 0 and sum(repv) == maxr and maxr > 1:
            return False
        else:
            return True

    return False



def get_diff(code):
    d = []
    for i in range(1, 6):
        d0 = int(code[i - 1])
        d1 = int(code[i])
        diff = d1 - d0
        if diff == 0:
            d.append(0)
        else:  # Normalize
            d.append(1)

    return d


def is_increasing(code):
    # Convert to six ints
    d0 = int(code[0])
    d1 = int(code[1])
    d2 = int(code[2])
    d3 = int(code[3])
    d4 = int(code[4])
    d5 = int(code[5])
    return d5 >= d4 >= d3 >= d2 >= d1 >= d0


seq = [171309, 643603]

test = [112233, 111122, 111134]
if __name__ == "__main__":
    print("run")
    # Fact: 6 digit code between seq[0] and seq[1]
    nr_possible_codes = seq[1] - seq[0]
    possibles = 0
    print("Number of codes: ", nr_possible_codes)

    for code in range(seq[0], seq[1]):
    #for code in test:
        if not is_increasing(str(code)):
            # Not increasing from left to right - invalid code
            nr_possible_codes -= 1
            continue
        elif not check_adjacent_groups(str(code)):
            # Check: Two adjacent digits are the same
            nr_possible_codes -= 1
            continue
        else:
            possibles += 1

    print("Number of possible codes: ", nr_possible_codes)
    print(possibles)
    # 853, 959, 1133 - wrong!