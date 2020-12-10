import re
import time

def removeCarriage(line):
    return line.strip('\n')

def setup(f):
    instruction_set, count = {}, 0
    for line in f:
        subset = line.split(' ')
        instruction_set[count] = [subset[0]] + [subset[1][0]] + [int(re.sub("\D", "", subset[1]))] + [0]
        count += 1
    return instruction_set
    
def run1():
    f = open("day8.txt", "r") 
    accumulator, current_position = 0, 0
    instruction_set = setup(f)
    last_cell = len(instruction_set.keys()) - 1
    while(True):
        instruction = instruction_set[current_position]
        if instruction[3] == 1: break
        if instruction[0] == 'acc':
            if instruction[1] == '+': accumulator += instruction[2]
            else: accumulator -= instruction[2]
            instruction_set[current_position][3] += 1
            current_position += 1
        elif instruction[0] == 'jmp':
            instruction_set[current_position][3] += 1
            if instruction[1] == '+': current_position += instruction[2]
            else: current_position -= instruction[2]
        else: 
            instruction_set[current_position][3] += 1
            current_position += 1
    f.close()
    print(accumulator)

def check(changed, instruction_set, operation, symbol, value, current_position, accumulator, last_cell):
    while(True):
        if operation == 'acc':
            print('test')
            if symbol == '+': accumulator += value
            else: accumulator -= value
            instruction_set[current_position][3] += 1
            current_position += 1
            # If accumular was the first input
            if changed: 
                return current_position, instruction_set, accumulator
        elif operation == 'jmp':
            if changed:
                instruction_set[current_position][3] += 1
                if current_position + 1 > last_cell: return current_position + 1, instruction_set, accumulator
                next_instruction = instruction_set[current_position + 1]
                return check(False, instruction_set, next_instruction[0], next_instruction[1], next_instruction[2], current_position + 1, accumulator, last_cell)
            instruction_set[current_position][3] += 1
            if symbol == '+': current_position += value
            else: current_position -= value
        else: 
            if changed:
                instruction_set[current_position][3] += 1
                if symbol == '+': current_position += value
                else: current_position -= value
                if current_position > last_cell: return current_position, instruction_set, accumulator
                next_instruction = instruction_set[current_position]
                return check(False, instruction_set, next_instruction[0], next_instruction[1], next_instruction[2], current_position, accumulator, last_cell)
            instruction_set[current_position][3] += 1
            current_position += 1
        if current_position > last_cell: return current_position, instruction_set, accumulator
        instruction = instruction_set[current_position]
        # Failed check
        if instruction[3] == 1: return -1, {}, 0
        operation, symbol, value, passed = instruction

def run2():
    f = open("day8.txt", "r") 
    accumulator, current_position = 0, 0
    instruction_set = setup(f)
    last_cell = len(instruction_set.keys()) - 1
    while(True):
        if current_position > last_cell: break
        instruction = instruction_set[current_position]
        current_position_c, instruction_set_c, accumulator_c = check(True, instruction_set, instruction[0], instruction[1], instruction[2], current_position, accumulator, last_cell)
        if current_position_c == -1:
            if instruction[0] == 'jmp':
                instruction_set[current_position][3] += 1
                if instruction[1] == '+': current_position += instruction[2]
                else: current_position -= instruction[2]
            else: 
                instruction_set[current_position][3] += 1
                current_position += 1
    
    
    f.close()
    print(accumulator)

def main():
    run1()
    #run2()

if __name__ == "__main__":
    main()