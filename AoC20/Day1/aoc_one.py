test_in = [1721, 979, 366, 299, 675, 1456]

if __name__ == '__main__':
    # Int needed to sum to 2020
    # tst = [2020-num for num in test_in]

    digits = []
    f = open("inputOne.txt", "r")
    for line in f:
        digits.append(int(line))

    # Part 1: Find two numbers in input that sum to 2020
    # Needed to sum to 2020
    neededForSum = [2020 - num for num in digits]

    nrs = []
    for val in neededForSum:
        fnd = val in digits
        if fnd:
            print('Found: {0}'.format(val))
            nrs.append(val)

    print('Product is: {0}'.format(nrs[0] * nrs[1]))

    # Part 2: Find three numbers in input that sum to 2020
    # So, find three elements in input who's sum is 2020
    found = False
    for i in range(len(digits)):
        first = digits[i]  # Lock it
        if found:
            break
        for j in range(len(digits)):
            if found:
                break
            for k in range(len(digits)):
                if found:
                    break
                # Test add with all other elements
                sums = first + digits[j] + digits[k]
                if sums == 2020:
                    print("Sum reached! {0}, {1}, {2}".format(digits[i], digits[j], digits[k]))
                    print("Product: {}".format(digits[i]*digits[j]*digits[k]))
                    found = True
