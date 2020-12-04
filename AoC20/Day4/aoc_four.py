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
    list_of_passport_dicts.append(dictionary)
    # For every passport (dict) in the list:
    valid_indices = []
    number_of_valid_passports = 0
    number_of_invalid_passports = 0
    for i, passport in enumerate(list_of_passport_dicts):
        keys = passport.keys()
        # 8 number of keys is a valid passport!
        if len(keys) == 8:
            number_of_valid_passports += 1
            valid_indices.append(i)
        elif len(keys) == 7 and 'cid' not in passport:
            # Also a valid passport
            number_of_valid_passports += 1
            valid_indices.append(i)
        else:
            # False passport
            number_of_invalid_passports += 1

    print("Number of valid passports after first check: {}".format(number_of_valid_passports))
    number_of_valid_passports = 0
    # Part two includes further checking!
    valid_eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for index in valid_indices:
        passport = list_of_passport_dicts[index]
        # Birth year [1920 - 2020]
        byr = int(passport['byr'])
        if not 1920 <= byr <= 2020:
            # Invalid birth year
            continue

        # Issue year [2010 - 2020]
        iyr = int(passport['iyr'])
        if not 2010 <= iyr <= 2020:
            continue

        # Expiration year [2020 - 2030]
        eyr = int(passport['eyr'])
        if not 2020 <= eyr <= 2030:
            continue

        # Height cm [150 193], in [59 76]
        hgt = passport['hgt']
        if hgt[-2:] == 'cm':
            if not 150 <= int(hgt[:-2]) <= 193:
                continue
        elif hgt[-2:] == 'in':
            if not 59 <= int(hgt[:-2]) <= 76:
                continue
        else:
            # Invalid
            continue

        hcl = passport['hcl']

        if hcl[0] != '#':
            continue
        try_hex = '0x' + hcl[1:]
        try:
            is_int = int(try_hex, 16)
        except:
            print("no hex in HCL")
            continue

        if passport['ecl'] not in valid_eye_color:
            continue

        # Passport ID, 9 digits, first must be zero
        pid = passport['pid']
        if not len(pid) == 9:
            continue
        to_sum = pid.split()[0]
        try:
            for element in to_sum:
                is_int = int(element)
        except:
            print("not int in PID")
            continue

        number_of_valid_passports += 1

    print("Number of valid passports after 2nd check: {}".format(number_of_valid_passports))
