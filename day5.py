
def removeCarriage(line):
    return line.strip('\n')

def run():
    f = open("day5.txt", "r")
    row, column = 0, 0
    dictionary = {}
    for line in f:
        line = removeCarriage(line)
        for index in range(len(line)):
            bw_position = len(line) - index - 1
            if(bw_position > 6):
                if(line[bw_position] == 'R'):
                    column += 2**index
            else:
                if(line[bw_position] == 'B'):
                    row += 2**(index-3)
        dictionary[(row * 8 + column)] = 1
        row, column = 0, 0

    for key in range(0, 1000):
        if key not in dictionary.keys():
            print(key)

def main():
    run()

if __name__ == "__main__":
    main()