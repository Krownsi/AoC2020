
def run_part_1():
    f = open("day12.txt", "r")
    instruction_set = [(line.strip()) for line in f.readlines() if line.strip()]
    vertical, horizontal, direction = 0, 0, 0
    for instruction in instruction_set:
        inst, value = instruction[0], int(instruction[1:len(instruction)])
        if inst == 'N': vertical += value
        elif inst == 'S': vertical -= value
        elif inst == 'E': horizontal += value
        elif inst == 'W': horizontal -= value
        elif inst == 'F': 
            if direction == 0: horizontal += value
            elif direction == 90: vertical += value
            elif direction == 180: horizontal -= value
            elif direction == 270: vertical -= value
        elif inst == 'L': direction = (direction + value) % 360
        elif inst == 'R': direction = (direction - value + 360) % 360
    print(abs(vertical) + abs(horizontal))

def run_part_2(starting):
    f = open("day12.txt", "r")
    instruction_set = [(line.strip()) for line in f.readlines() if line.strip()]
    vertical, horizontal, waypoint = 0, 0, starting.copy()
    for instruction in instruction_set:
        inst, value = instruction[0], int(instruction[1:len(instruction)])
        if inst == 'N': waypoint[1] += value
        elif inst == 'S': waypoint[1] -= value
        elif inst == 'E': waypoint[0] += value
        elif inst == 'W': waypoint[0] -= value
        elif inst == 'F': 
            vertical += waypoint[1] * value
            horizontal += waypoint[0] * value
        elif inst == 'R': 
            if value == 90: waypoint = [waypoint[1], waypoint[0] * -1]
            elif value == 180: waypoint = [waypoint[0] * -1, waypoint[1] * -1]
            else: waypoint = [waypoint[1] * -1, waypoint[0]]
        elif inst == 'L': 
            if value == 90: waypoint = [waypoint[1] * -1, waypoint[0]]
            elif value == 180: waypoint = [waypoint[0] * -1, waypoint[1] * -1]
            else: waypoint = [waypoint[1], waypoint[0] * -1]
    print(abs(vertical) + abs(horizontal))

def main():
    # run_part_1()
    # E/W, N/S
    waypoint = [10, 1]
    run_part_2(waypoint)

if __name__ == "__main__":
    main()