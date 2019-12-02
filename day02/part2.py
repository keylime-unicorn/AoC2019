import sys

for line in sys.stdin:
    original = list([int(x) for x in line.split(",")])

    #replace values in 1 and 2
    for j in range(0,100):
        for k in range(0,100):
            new = original[:]
            new[1] = j
            new[2] = k

            nxt = 0
            for i in range(len(new)):
                if nxt == i:
                    opcode = new[i]
                else: 
                    continue

                if opcode == 1:
                    new[new[i+3]] = new[new[i+1]] + new[new[i+2]]  
                    nxt = i+4
                elif opcode == 2:
                    new[new[i+3]] = new[new[i+1]] * new[new[i+2]]  
                    nxt = i+4
                elif opcode == 99:
                    break
                else:
                    print("ERROR: ", opcode)
        
            if new[0] == 19690720:
                break
        
        if new[0] == 19690720:
            break

    print(j,k)
    answer = 100 * j + k
    print(answer)
