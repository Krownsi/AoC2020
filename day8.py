import re
import time

def removeCarriage(line):
    return line.strip('\n')

def run(part):
    f = open("day8.txt", "r") 
    instruction_set, accumulator, current_position, count = {}, 0, 0, 0
    for line in f:
        subset = line.split(' ')
        instruction_set[count] = [subset[0]] + [subset[1][0]] + [int(re.sub("\D", "", subset[1]))] + [0]
        count += 1
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
            next_instruction = instruction_set[current_position + 1]
            instruction_set[current_position][3] += 1
            if instruction[1] == '+': current_position += instruction[2]
            else: current_position -= instruction[2]
        else: 
            instruction_set[current_position][3] += 1
            current_position += 1
    f.close()
    print(accumulator)

def run2():
    f = open("day8.txt", "r") 
    instruction_set, accumulator, current_position, count = {}, 0, 0, 0
    for line in f:
        subset = line.split(' ')
        instruction_set[count] = [subset[0]] + [subset[1][0]] + [int(re.sub("\D", "", subset[1]))] + [0]
        count += 1
    last_cell = len(instruction_set.keys()) - 1
    while(True):
        if current_position > last_cell: break
        instruction = instruction_set[current_position]
        if instruction[3] == 1: break
        if instruction[0] == 'acc':
            if instruction[1] == '+': accumulator += instruction[2]
            else: accumulator -= instruction[2]
            instruction_set[current_position][3] += 1
            current_position += 1
        elif instruction[0] == 'jmp':
            next_instruction = instruction_set[current_position + 1]
            if((current_position + 2 > last_cell and (next_instruction[0] == 'acc' or next_instruction[0] == 'nop')) or (next_instruction[0] == 'jmp' and next_instruction[1] == '+' and next_instruction[2] + current_position + 1 > last_cell)):
                current_position += 1
                continue
            instruction_set[current_position][3] += 1
            if instruction[1] == '+': current_position += instruction[2]
            else: current_position -= instruction[2]
        else: 
            new_current = current_position
            if instruction[1] == '+': new_current += instruction[2]
            else: new_current -= instruction[2]
            next_instruction = instruction_set[new_current]
            if((new_current + 2 > last_cell and (next_instruction[0] == 'acc' or next_instruction[0] == 'nop')) or (next_instruction[0] == 'jmp' and next_instruction[1] == '+' and next_instruction[2] + new_current > last_cell)):
                current_position = new_current
                continue
            instruction_set[current_position][3] += 1
            current_position += 1
    f.close()
    print(accumulator)

def main():
    #run1()
    run2()

if __name__ == "__main__":
    main()