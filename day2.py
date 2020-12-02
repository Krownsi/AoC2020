
def removeCarriage(line):
    if "\n" in line:
        return line.strip('\n')
    return line

def setup_input(line):
    # Get rid of carriage return
    line = removeCarriage(line)
    # Split password from policy
    split_line = line.split(": ")
    # Split range from char
    split_line[0] = split_line[0].split(" ")
    split_line[0][0] = split_line[0][0].split("-")
    return split_line

def number_of_char(char, password):
    count = 0
    for c in password:
        if c == char:
            count = count + 1
    return count

def in_range(count, min, max):
    if(count >= int(min) and count <= int(max)):
        return True

def question_1():
    # Open text file with inputs
    f = open("day2.txt", "r")
    good_passwords = 0
    for line in f:
        split_line = setup_input(line)
        char = split_line[0][1]
        count = number_of_char(char, split_line[1])
        if(in_range(count, split_line[0][0][0], split_line[0][0][1])):
            good_passwords = good_passwords + 1
    f.close()
    print(good_passwords)

def question_2():
    # Open text file with inputs
    f = open("day2.txt", "r")
    good_passwords = 0
    for line in f:
        split_line = setup_input(line)
        char = split_line[0][1]
        if((char == split_line[1][int(split_line[0][0][0]) - 1]) != (char == split_line[1][int(split_line[0][0][1]) - 1])):
            good_passwords = good_passwords + 1
    f.close()
    print(good_passwords)

def main():
    question_2()

if __name__ == "__main__":
    main()