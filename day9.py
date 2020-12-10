def setup():
    f = open("day9.txt", "r")
    numbers = [int(line.strip()) for line in f.readlines() if line.strip()]
    return numbers

def checkIfSum(value, rangeNumbers, size):
    for outer in range(size):
        if rangeNumbers[outer] >= value: continue
        for inner in range(outer + 1, size):
            if rangeNumbers[outer] + rangeNumbers[inner] == value: return True
    return False

def contiguous(numbers, value):
    currentRange, summation, internalRange = 0, 0, 0
    for cellValue in numbers[currentRange: (len(numbers)-1)]:
        if cellValue > value: 
            currentRange += 1
            continue
        for internalValue in numbers[currentRange: (len(numbers)-1)]:
            internalRange += 1
            if summation == value: 
                return numbers[currentRange:internalRange]
            if summation > value: 
                summation, internalRange = 0, currentRange
                currentRange += 1
                break
            summation += internalValue
    return []

def getMaxAndMin(rangeSum):
    minim, maxim = -1, -1
    for current in rangeSum:
        if minim == -1: minim, maxim = current, current
        elif current > maxim: maxim = current
        elif current < minim: minim = current
    return minim, maxim

def run():
    numbers, preamble, iterator, value = setup(), 25, 0, 0
    for current in range(preamble, len(numbers)):
        value, found = numbers[current], checkIfSum(numbers[current], numbers[current - preamble: current], preamble)
        if(not found): break
    rangeSum = contiguous(numbers, value)
    maxim, minim = getMaxAndMin(rangeSum)
    print(maxim + minim)

def main():
    run()
    
if __name__ == "__main__":
    main()