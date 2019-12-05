import sys

def get_parameters(program, i, modes):
    params = {}
    for j in range(1,3):
        if modes[j] == '0':
            try:
                params[j] = program[program[i+j]]
            except:
                params[j] = program[i+j]
        else:
            params[j] = program[i+j]

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

    nxt = 0
    input_int = 1

    for i in range(len(program)):

        if nxt == i:
            item = program[i]
        else: 
            continue

        a,b,c,d,e = get_opcode_and_parameter_modes(item)

        opcode = str(d) + str(e)
        modes = {}
        modes[1] = c
        modes[2] = b

        if opcode == '01':
            params = get_parameters(program, i, modes)
            program[program[i+3]] = params[1] + params[2]
            nxt = i+4
        elif opcode == '02':
            params = get_parameters(program, i, modes)
            program[program[i+3]] = params[1] * params[2]
            nxt = i+4
        elif opcode == '03':
            program[program[i+1]] = input_int
            nxt = i+2
        elif opcode == '04':
            params = get_parameters(program, i, modes)
            print(params[1])
            nxt = i+2
        elif opcode == '99':
            break
        else: 
            print("INCORRECT OPCODE: ", opcode)

    return program


def main():

    program = sys.stdin.readline()    

    program = program.strip().split(",")
    program = [int(x) for x in program]
    intcode_computer(program)

if __name__ == "__main__":
    main()
