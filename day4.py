import re

def removeCarriage(line):
    return line.strip('\n')

def validHeight(height):
    if 'cm' in height:
        cm_value = height.split('cm')
        if(int(cm_value[0]) >= 150 and int(cm_value[0]) <= 193):
            return 1
    if 'in' in height: 
        in_value = height.split('in')
        if(int(in_value[0]) >= 59 and int(in_value[0]) <= 76):
            return 1
    return 0

def check(passport, part):
    attributes = ['hcl', 'ecl', 'pid', 'eyr', 'byr', 'iyr', 'hgt']
    valid = True
    if(part == 1):
        valid = all(key in passport for key in attributes)
        if(valid):
            return 1
    elif(part == 2):
        if not all(key in passport for key in attributes):
            return 0
        valid = valid and len(passport['byr']) == 4 and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002
        valid = valid and len(passport['iyr']) == 4 and int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020
        valid = valid and len(passport['eyr']) == 4 and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030
        valid = valid and validHeight(passport['hgt'])
        valid = valid and re.search('^#([0-9]|[a-f]){6}$', passport['hcl'])
        valid = valid and passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        valid = valid and re.search('^[0-9]{9}$', passport['pid'])
    if valid: return 1
    return 0

def convertListToDic(passport):
    dictionary = {}
    for entity in passport:
        dictionary[entity[0]] = entity[1]
    return dictionary

def run(part):
    f = open("day4.txt", "r")
    passport = []
    valid_passports = 0
    for line in f:
        line = removeCarriage(line).split()
        if(line == []):
            passport = map(lambda x: x.split(':'), passport)
            valid_passports += check(convertListToDic(list(passport)), part)
            passport = []
        passport += line
    passport = map(lambda x: x.split(':'), passport)
    valid_passports += check(convertListToDic(list(passport)), part)
    f.close()
    return valid_passports

def main():
    print(run(1))
    print(run(2))

if __name__ == "__main__":
    main()