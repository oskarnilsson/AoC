if __name__ == "__main__":
    f = open("day4.txt", "r")
    list_of_passport_dicts = []
    dictionary = {}

    for lines in f:
        if lines != '\n':  # Parsing passport
            s = lines.split(' ')
            # Remove escape char and newline
            s[-1] = s[-1][:-1]
            for str in s:
                keyvalue = str.split(':')
                dictionary[keyvalue[0]] = keyvalue[1]
        else:  # New passport
            list_of_passport_dicts.append(dictionary)
            dictionary = {}

    # For every passport (dict) in the list:
    number_of_valid_passports = 0
    number_of_invalid_passports = 0
    for passport in list_of_passport_dicts:
        keys = passport.keys()
        # 8 number of keys is a valid passport!
        if len(keys) == 8:
            number_of_valid_passports += 1
        elif len(keys) == 7 and 'cid' not in passport:
            # Also a valid passport
            number_of_valid_passports += 1
        else:
            # False passport
            number_of_invalid_passports += 1

    print("Number of valid passports: {}".format(number_of_valid_passports))
