import sys
import math

wire_1 = [(0,0)]
wire_2 = [(0,0)]

def go_up(wire, num):
    for n in range(num):
        pair = (wire[-1][0], wire[-1][1] + 1)
        wire.append(pair)

def go_right(wire, num):
    for n in range(num):
        pair = (wire[-1][0] + 1, wire[-1][1])
        wire.append(pair)

def go_down(wire, num):
    for n in range(num):
        pair = (wire[-1][0], wire[-1][1] - 1)
        wire.append(pair)

def go_left(wire, num):
    for n in range(num):
        pair = (wire[-1][0] - 1, wire[-1][1])
        wire.append(pair)

def get_wire_path(wire, path):
    path = path.split(",")

    for p in path:
        if p[0] == "U":
            go_up(wire, int(p[1:]))
        elif p[0] == "R":
            go_right(wire, int(p[1:]))
        elif p[0] == "D":
            go_down(wire, int(p[1:]))
        elif p[0] == "L":
            go_left(wire, int(p[1:]))

def get_crossings():
    return list(set(wire_1) & set(wire_2))

def get_manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1]) 

def distance(a,b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def is_between(a,c,b):
    return distance(a,c) + distance(c,b) == distance(a,b)

def get_steps(c):
    wire1 = 0
    wire2 = 0

    m = 0

    for i, p in enumerate(wire_1[:-1]):

        q = wire_1[i+1]

        if is_between(p,c,q):
            m += get_manhattan(p,c)
            break
        else:
            m += get_manhattan(p,q)

    for i, p in enumerate(wire_2[:-1]):

        q = wire_2[i+1]

        if is_between(p,c,q):
            m += get_manhattan(p,c)
            break
        else:
            m += get_manhattan(p,q)

    return m

def main():

    smallest = float('inf')

    wire1 = sys.stdin.readline()
    wire2 = sys.stdin.readline() 

    wire1_path = get_wire_path(wire_1, wire1)
    wire2_path = get_wire_path(wire_2, wire2)

    crossings = get_crossings()
    crossings.remove((0,0))

    for coordinate in crossings:
        steps = get_steps(coordinate)
        if steps < smallest:
            smallest = steps

    print(smallest)

if __name__ == "__main__":
    main()
