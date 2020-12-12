import copy

def setup():
    f = open("day11.txt", "r")
    seats = []
    for line in f:
        seats += [['0'] + [char for char in line.strip()] + ['0']]
    seats = [[char for char in '0' * len(seats[0])]] + seats + [[char for char in '0' * len(seats[0])]]
    f.close()
    return seats

def countAdj(x, y, seats):
    testing_array = []
    testing_array += seats[x+1][y]
    testing_array += seats[x][y+1]
    testing_array += seats[x+1][y+1]
    testing_array += seats[x][y-1]
    testing_array += seats[x+1][y-1]
    testing_array += seats[x-1][y-1]
    testing_array += seats[x-1][y]
    testing_array += seats[x-1][y+1]
    return list(map(lambda char: char == '#', testing_array))

def updateL(x, y, seats):
    valid = sum(countAdj(x, y , seats))
    if valid == 0: return '#'
    return 'L'

def updateH(x, y, seats):
    value = sum(countAdj(x, y , seats))
    if value >= 4: return 'L'
    return '#'

def numberOfOccupied(seat_arrangment):
    total = 0
    for row in seat_arrangment:
        total += sum(map(lambda char: char == "#", row))
    return total

def part1():
    seats, dynamic_seats = setup(), setup()
    while(True):
        for row in range(1, len(seats)-1):
            for column in range(1, len(seats[0])-1):
                if seats[row][column] == 'L': dynamic_seats[row][column] = updateL(row, column, seats)
                if seats[row][column] == '#': dynamic_seats[row][column] = updateH(row, column, seats)
        if numberOfOccupied(seats) == numberOfOccupied(dynamic_seats): break
        seats = copy.deepcopy(dynamic_seats)
    return numberOfOccupied(seats)

def countAdj2(x, y, seats):
    testing_array = []
    
    for inc in range(1, 10000):
        if seats[x+inc][y] == "#" or seats[x+inc][y] == "L" or seats[x+inc][y] == "0": 
            testing_array += seats[x+inc][y]
            break
    for inc in range(1, 10000):
        if seats[x-inc][y] == "#" or seats[x-inc][y] == "L" or seats[x-inc][y] == "0": 
            testing_array += seats[x-inc][y]
            break
    for inc in range(1, 10000):
        if seats[x][y+inc] == "#" or seats[x][y+inc] == "L" or seats[x][y+inc] == "0": 
            testing_array += seats[x][y+inc]
            break
    for inc in range(1, 10000):
        if seats[x][y-inc] == "#" or seats[x][y-inc] == "L" or seats[x][y-inc] == "0": 
            testing_array += seats[x][y-inc]
            break
    for inc in range(1, 10000):
        if seats[x-inc][y-inc] == "#" or seats[x-inc][y-inc] == "L" or seats[x-inc][y-inc] == "0": 
            testing_array += seats[x-inc][y-inc]
            break
    for inc in range(1, 10000):
        if seats[x+inc][y+inc] == "#" or seats[x+inc][y+inc] == "L" or seats[x+inc][y+inc] == "0": 
            testing_array += seats[x+inc][y+inc]
            break
    for inc in range(1, 10000):
        if seats[x+inc][y-inc] == "#" or seats[x+inc][y-inc] == "L" or seats[x+inc][y-inc] == "0": 
            testing_array += seats[x+inc][y-inc]
            break
    for inc in range(1, 10000):
        if seats[x-inc][y+inc] == "#" or seats[x-inc][y+inc] == "L" or seats[x-inc][y+inc] == "0": 
            testing_array += seats[x-inc][y+inc]
            break
    return list(map(lambda char: char == '#', testing_array))

def updateL2(x, y, seats):
    valid = sum(countAdj2(x, y , seats))
    if valid == 0: return '#'
    return 'L'

def updateH2(x, y, seats):
    value = sum(countAdj2(x, y , seats))
    if value >= 5: return 'L'
    return '#'

def part2():
    seats, dynamic_seats = setup(), setup()
    while(True):
        for row in range(1, len(seats)-1):
            for column in range(1, len(seats[0])-1):
                if seats[row][column] == 'L': dynamic_seats[row][column] = updateL2(row, column, seats)
                if seats[row][column] == '#': dynamic_seats[row][column] = updateH2(row, column, seats)
        if numberOfOccupied(seats) == numberOfOccupied(dynamic_seats): break
        seats = copy.deepcopy(dynamic_seats)
    return numberOfOccupied(seats)

def main():
    # print(part1())
    print(part2())

if __name__ == "__main__":
    main()
