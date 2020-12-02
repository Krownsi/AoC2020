
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

def breakdown(input):
    char = input[0][1]
    int_range = input[0][0]
    min = int_range[0]
    max = int_range[1]
    return input[1], char, min, max

def question_1():
    # Open text file with inputs
    f = open("day2.txt", "r")
    good_passwords = 0
    for line in f:
        split_line = setup_input(line)
        password, char, min, max = breakdown(split_line)
        count = number_of_char(char, password)
        if(in_range(count, min, max)):
            good_passwords = good_passwords + 1
    f.close()
    print(good_passwords)

def question_2():
    # Open text file with inputs
    f = open("day2.txt", "r")
    good_passwords = 0
    for line in f:
        split_line = setup_input(line)
        password, char, min, max = breakdown(split_line)
        if((char == password[int(min) - 1]) != (char == password[int(max) - 1])):
            good_passwords = good_passwords + 1
    f.close()
    print(good_passwords)

def main():
    question_2()

if __name__ == "__main__":
    main()