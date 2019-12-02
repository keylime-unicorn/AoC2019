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
        for j in range(0,100):
            for k in range(0,100):
                line[1] = j
                line[2] = k

                result = intcode_computer(line[:])
                if result[0] == 19690720:
                    break

            if result[0] == 19690720:
                break

        answer = 100 * j + k
        print(answer)

if __name__ == "__main__":
    main()
