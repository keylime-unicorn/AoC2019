import sys

def intcode_computer(program):

    nxt = 0

    for i in range(len(program)):
        if nxt == i:
            opcode = program[i]
        else: 
            continue

        if opcode == 1:
            program[program[i+3]] = program[program[i+1]] + program[program[i+2]]  
            nxt = i+4
        elif opcode == 2:
            program[program[i+3]] = program[program[i+1]] * program[program[i+2]]  
            nxt = i+4
        elif opcode == 99:
            break

    return program

def main():
    
    for line in sys.stdin:
        line = list([int(x) for x in line.split(",")])

        #set up program
        line[1] = 12
        line[2] = 2

        result = intcode_computer(line[:])

        print(result[0])

if __name__ == "__main__":
    main()
