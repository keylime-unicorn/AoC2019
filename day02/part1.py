import sys

for line in sys.stdin:
    line = list([int(x) for x in line.split(",")])

    print(line)

    nxt = 0
    for i in range(len(line)):
        if nxt == i:
            opcode = line[i]
        else: 
            continue

        if opcode == 1:
            line[line[i+3]] = line[line[i+1]] + line[line[i+2]]  
            nxt = i+4
        elif opcode == 2:
            line[line[i+3]] = line[line[i+1]] * line[line[i+2]]  
            nxt = i+4
        elif opcode == 99:
            break
        else:
            print("ERROR: ", opcode)

    print(line)
