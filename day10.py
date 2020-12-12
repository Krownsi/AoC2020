import math

def setup():
    f = open("day10.txt", "r")
    numbers = [int(line.strip()) for line in f.readlines() if line.strip()]
    numbers = [0] + numbers + [max(numbers) + 3]
    f.close()
    return numbers

def part(numbers):
    ones, threes, last, part2 = 0, 0, 0, [1]
    for key in numbers:
        if key - last == 1: ones += 1
        elif key - last == 3: threes += 1
        last = key
    print('Q1: ' + str(ones * threes))
    for i in range(numbers[1], len(numbers)):
        ans = 0
        for j in range(i):
            if numbers[j] + 3 >= numbers[i]: ans += part2[j]
        part2 += [ans]
    print('Q2: ' + str(part2[-1]))

def run():
    numbers = list(set(setup()))
    numbers.sort()
    part(numbers)

def main():
    run()
    
if __name__ == "__main__":
    main()