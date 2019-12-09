import sys

relative_base = 0

def get_parameters(program, i, modes):
    params = {}

    for j in range(1,4):
        if modes[j] == '0':
            if (i+j) >= len(program):
                missing = (i+j) - len(program)
                for _ in range(missing+1):
                    program.append(0)
            if program[i+j] >= len(program):
                missing = program[i+j] - len(program)
                for _ in range(missing+1):
                    program.append(0)
            params[j] = program[program[i+j]]
        elif modes[j] == '1':
            params[j] = program[i+j]
        elif modes[j] == '2':
            if (relative_base+program[i+j]) >= len(program):
                missing = (relative_base+program[i+j]) - len(program)
                for _ in range(missing+1):
                    program.append(0)
            params[j] = program[relative_base+program[i+j]]
#    print("modes:", modes, " -- params:", params)

    return params


def get_opcode_and_parameter_modes(item):

    item = [x for x in str(item)]
    item.reverse()
    if len(item) < 5:
        for _ in range(5-len(item)):
            item.append('0')

    item.reverse()

    return item


def intcode_computer(program):

    i = 0
    input_int = 1

    global relative_base
    
    while i < len(program)-1:

        item = program[i]

        nxt = i

        a,b,c,d,e = get_opcode_and_parameter_modes(item)

        opcode = str(d) + str(e)
        modes = {}
        modes[1] = c
        modes[2] = b
        modes[3] = a

        params = {}

        #increase program size
        if opcode == '01' or opcode == '02' or opcode == '07' or opcode == '08':
            if program[i+3] >= len(program):
                missing = program[i+3] - len(program)
                for _ in range(missing+1):
                    program.append(0)
            if (relative_base+program[i+3]) >= len(program):
                missing = relative_base + program[i+3] - len(program)
                for _ in range(missing+1):
                    program.append(0)
        if opcode == '03': 
            if program[i+1] >= len(program):
                missing = program[i+1] - len(program)
                for _ in range(missing+1):
                    program.append(0)
            if (relative_base+program[i+1]) >= len(program):
                missing = relative_base + program[i+1] - len(program)
                for _ in range(missing+1):
                    program.append(0)

#        print(opcode)

        #check opcodes
        if opcode == '01':
            params = get_parameters(program, i, modes)
            if modes[3] == '0':
                program[program[i+3]] = params[1] + params[2]
            else:
                program[relative_base+program[i+3]] = params[1] + params[2]
            i = i+4
        elif opcode == '02':
            params = get_parameters(program, i, modes)
            if modes[3] == '0':
                program[program[i+3]] = params[1] * params[2]
            else:
                program[relative_base+program[i+3]] = params[1] * params[2]
            i = i+4
        elif opcode == '03':
            if modes[1] == '0':
                program[program[i+1]] = input_int
            else:
                program[relative_base+program[i+1]] = input_int
            i = i+2
        elif opcode == '04':
            params = get_parameters(program, i, modes)
            print(params[1])
            i = i+2
        elif opcode == '05':
            params = get_parameters(program, i, modes)
            if params[1] != 0:
                i = params[2]
            else:
                i = i+3
        elif opcode == '06':
            params = get_parameters(program, i, modes)
            if params[1] == 0:
                i = params[2]
            else:
                i = i+3
        elif opcode == '07':
            params = get_parameters(program, i, modes)
            if params[1] < params[2]:
                if modes[3] == '0':
                    program[program[i+3]] = 1
                else:
                    program[relative_base+program[i+3]] = 1
            else: 
                if modes[3] == '0':
                    program[program[i+3]] = 0
                else:
                    program[relative_base+program[i+3]] = 0
            i = i+4
        elif opcode == '08':
            params = get_parameters(program, i, modes)
            if params[1] == params[2]:
                if modes[3] == '0':
                    program[program[i+3]] = 1
                else:
                    program[relative_base+program[i+3]] = 1
            else: 
                if modes[3] == '0':
                    program[program[i+3]] = 0
                else:
                    program[relative_base+program[i+3]] = 0
            i = i+4
        elif opcode == '09':
            params = get_parameters(program, i, modes)
            relative_base += params[1]
            i = i+2
        elif opcode == '99':
            break
        else: 
            print("INCORRECT OPCODE: ", opcode)

    return 


def main():

    program = sys.stdin.readline().strip()
    program = [int(x) for x in program.split(",")]    

    intcode_computer(program)


if __name__ == "__main__":
    main()
