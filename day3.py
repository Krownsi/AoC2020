
def removeCarriage(line):
    return line.strip('\n')

def collisions(incrementor, input_lines):
    f = open("day3.txt", "r")
    index_right, number_of_trees, count = 0, 0, 0
    for line in f:
        if count % input_lines == 0:
            line = removeCarriage(line)
            index_right %= len(line)
            if line[index_right] == "#": number_of_trees += 1
            index_right += incrementor
        count += 1

    f.close()

    return number_of_trees

def question_2():
    mult_collisions = 1
    incrementor = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for index in incrementor:
        mult_collisions *= collisions(index[0], index[1])
    print(mult_collisions)
    
def question_1():
    print(collisions(3, 1))

def main():
    question_1()
    question_2()

if __name__ == "__main__":
    main()