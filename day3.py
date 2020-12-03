
def removeCarriage(line):
    if "\n" in line:
        return line.strip('\n')
    return line

def collisions(incrementor, input_lines):
    f = open("day3.txt", "r")
    index_right, number_of_trees, count = 0, 0, 1
    for line in f:
        count += 1
        if count % input_lines == 0:
            line = removeCarriage(line)
            if len(line) <= index_right: index_right %= len(line)
            if line[index_right] == "#": number_of_trees += 1
            index_right += incrementor

    f.close()

    return number_of_trees

def question_2():
    incrementor = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for index in incrementor:
        mult_collisions = mult_collisions * collisions(index[0], index[1])
    print(mult_collisions)
    
def question_1():
    print(collisions(3, 1))

def main():
    question_1()

if __name__ == "__main__":
    main()