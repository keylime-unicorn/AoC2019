import sys

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

def get_manhattan(coordinate):
    return abs(coordinate[0]) + abs(coordinate[1]) 

def main():

    smallest = float('inf')

    wire1 = sys.stdin.readline()
    wire2 = sys.stdin.readline() 

    wire1_path = get_wire_path(wire_1, wire1)
    wire2_path = get_wire_path(wire_2, wire2)

    crossings = get_crossings()
    crossings.remove((0,0))

    for coordinate in crossings:
        manhattan = get_manhattan(coordinate)
        if manhattan < smallest:
            smallest = manhattan

    print(smallest)

if __name__ == "__main__":
    main()
