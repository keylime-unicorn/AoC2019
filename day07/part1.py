import sys
import itertools

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


def intcode_computer(program, first, second):

    nxt = 0
    first_input = True

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

        params = {}

        if opcode == '01':
            params = get_parameters(program, i, modes)
            program[program[i+3]] = params[1] + params[2]
            nxt = i+4
        elif opcode == '02':
            params = get_parameters(program, i, modes)
            program[program[i+3]] = params[1] * params[2]
            nxt = i+4
        elif opcode == '03':
            if first_input:
                program[program[i+1]] = first
                first_input = False
            else:
                program[program[i+1]] = second
            nxt = i+2
        elif opcode == '04':
            params = get_parameters(program, i, modes)
#            print(params[1])
            return_val = params[1]
            nxt = i+2
        elif opcode == '05':
            params = get_parameters(program, i, modes)
            if params[1] != 0:
                nxt = params[2]
            else:
                nxt = i+3
        elif opcode == '06':
            params = get_parameters(program, i, modes)
            if params[1] == 0:
                nxt = params[2]
            else:
                nxt = i+3
        elif opcode == '07':
            params = get_parameters(program, i, modes)
            if params[1] < params[2]:
                program[program[i+3]] = 1
            else: 
                program[program[i+3]] = 0
            nxt = i+4
        elif opcode == '08':
            params = get_parameters(program, i, modes)
            if params[1] == params[2]:
                program[program[i+3]] = 1
            else: 
                program[program[i+3]] = 0
            nxt = i+4
        elif opcode == '99':
            break
        else: 
            print("INCORRECT OPCODE: ", opcode)

    return return_val


phase_settings = [0, 1, 2, 3, 4]

def main():

    max_thrust = 0
    permutations = itertools.permutations(phase_settings)

    line = sys.stdin.readline().strip().split(",")

    for permutation in permutations:

        program = [int(x) for x in line[:]]

        amp_a = intcode_computer(program, permutation[0], 0)
        amp_b = intcode_computer(program, permutation[1], amp_a)
        amp_c = intcode_computer(program, permutation[2], amp_b)
        amp_d = intcode_computer(program, permutation[3], amp_c)
        amp_e = intcode_computer(program, permutation[4], amp_d)
        
        if amp_e > max_thrust:
            max_thrust = amp_e

    print(max_thrust)


if __name__ == "__main__":
    main()
