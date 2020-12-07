def removeCarriage(line):
    return line.strip('\n')

def countYes(inputValue):
    listOfChars = {}
    similar = 0;
    for people in inputValue:
        for char in people:
            if char in listOfChars: listOfChars[char] += 1
            else: listOfChars[char] = 1
    result = map(lambda x: 1 if listOfChars[x] == len(inputValue) else 0, listOfChars.keys())
    return sum(result)

def run():
    f = open("day6.txt", "r")
    answer = []
    sum = 0
    for line in f:
        line = removeCarriage(line).split()
        if(line == []):       
            sum += countYes(answer)
            answer = []
        answer += line
    sum += countYes(answer)
    print(sum)

def main():
    run()

if __name__ == "__main__":
    main()