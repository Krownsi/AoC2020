def setup():
    f = open("day9.txt", "r")
    numbers = [int(line.strip()) for line in f.readlines() if line.strip()]
    return numbers

def checkIfSum(value, rangeNumbers, size):
    for outer in range(size):
        if rangeNumbers[outer] >= value: continue
        elif any(map(lambda inner: rangeNumbers[outer] + rangeNumbers[inner] == value, range(outer + 1, size))): return True
    return False

def contiguous(numbers, value):
    summation, goodSum = 0, []
    for outerCell in enumerate(numbers):
        if outerCell[1] > value: 
            continue
        for internalCell in enumerate(numbers[outerCell[0]: (len(numbers)-1)]):
            if summation == value: 
                return goodSum
            elif summation > value: 
                goodSum, summation = [], 0
                break
            summation += internalCell[1]
            goodSum += [internalCell[1]]

def run():
    numbers, preamble, iterator, value = setup(), 25, 0, 0
    for current in range(preamble, len(numbers)):
        value, found = numbers[current], checkIfSum(numbers[current], numbers[current - preamble: current], preamble)
        if(not found): break
    print('Q1: ' + str(value))
    rangeSum = contiguous(numbers, value)
    print('Q2: ' + str(min(rangeSum) + max(rangeSum)))

def main():
    run()
    
if __name__ == "__main__":
    main()