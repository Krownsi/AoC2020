import re

def removeCarriage(line):
    return line.strip('\n')

def checkIfValidQ1(passport, score):
    str_passport = ''.join(passport)
    if ("hcl:" in str_passport) and ("ecl:" in str_passport) and ("pid:" in str_passport) and ("eyr:" in str_passport) and ("byr:" in str_passport) and ("iyr:" in str_passport) and ("hgt:" in str_passport):
        score += 1
    return score

def checkIfDatesValid(input):
    entity = input.split(':')
    if(len(entity) != 1):
        value = entity[1]
        length = len(value)
        key = entity[0]
        if key == 'byr' and length == 4 and int(value) >= 1920 and int(value) <= 2002:
            return 1
        elif key == 'iyr' and length == 4 and int(value) >= 2010 and int(value) <= 2020: 
            return 1
        elif key == 'eyr' and length == 4 and int(value) >= 2020 and int(value) <= 2030: 
            return 1
        elif key == 'hgt':
            if 'cm' in value:
                cm_value = value.split('cm')
                if(int(cm_value[0]) >= 150 and int(cm_value[0]) <= 193):
                    return 1
            if 'in' in value: 
                in_value = value.split('in')
                if(int(in_value[0]) >= 59 and int(in_value[0]) <= 76):
                    return 1
        elif key == 'hcl' and re.search('^#([0-9]|[a-f]){6}$', value):
            return 1
        elif key == 'ecl' and ('amb' == value or 'blu' == value or 'brn' == value or 'gry' == value or 'grn' == value or 'hzl' == value or 'oth' == value):
            return 1
        elif key == 'pid' and re.search('^[0-9]{9}$', value):
            return 1
    return 0

def checkIfValidQ2(passport, score):
    valid_list = map(checkIfDatesValid, passport)
    number_of_checks_passed = sum(list(valid_list))
    if(number_of_checks_passed == 7):
        score += 1
    return score

def run_logic(part):
    f = open("day4.txt", "r")
    passport = []
    valid_passports = 0
    for line in f:
        line = removeCarriage(line)
        if(line == ""):
            if(part == 1):
                valid_passports = checkIfValidQ1(passport, valid_passports)
            else:
                valid_passports = checkIfValidQ2(passport, valid_passports)
            passport = []
        passport += line.split(' ')
    if(part == 1):
        valid_passports = checkIfValidQ1(passport, valid_passports)
    else:
        valid_passports = checkIfValidQ2(passport, valid_passports)
    print(valid_passports)
    f.close()

def main():
    run_logic(2)
    run_logic(1)

if __name__ == "__main__":
    main()