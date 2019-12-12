import sys
import copy as dc
from math import atan2

asteroid_map = []

def pretty_print(mapp):
    for row in mapp:
        print(''.join(row))


def count_asteroids(copy):
    count = -1

    for row in copy:
        for item in row:
            if item != '.' and item != '-':
                count += 1

    return count


def is_visible(ogx, ogy, curx, cury, visible):

    dy = cury-ogy
    dx = curx-ogx

    current = atan2(dy, dx)

    for angle in visible:
        if current == angle:
            return False

    visible.append(current)
    return True


def mark_blind_spots(x, y, map_copy):
    visible = []

    j = x
    for item in map_copy[y][x+1:]:
        j += 1
        if item == ".":
            continue

        if not is_visible(x, y, j, y, visible):
            map_copy[y][j] = "-"

    j = x
    for item in map_copy[y][x-1::-1]:
        j -= 1
        if j<0:
            break

        if item == ".":
            continue

        if not is_visible(x, y, j, y, visible):
            map_copy[y][j] = "-"



    i = y-1
    for row in map_copy[y-1::-1]:
        if i < 0:
            break
        for j, item in enumerate(row):
            if item == ".":
                continue

            if not is_visible(x, y, j, i, visible):
                map_copy[i][j] = "-"
        i -= 1

    i = y+1
    for row in map_copy[y+1:]:
        for j, item in enumerate(row):
            if item == ".":
                continue

            if not is_visible(x, y, j, i, visible):
                map_copy[i][j] = "-"

        i += 1

    return


def main():
    
    max_visible = 0
    max_location = (0,0)

    global asteroid_map

    for line in sys.stdin:
        line = list([x for x in line.strip()])
        asteroid_map.append(line)

    for r, row in enumerate(asteroid_map):
        for c, item in enumerate(row):
            copy = dc.deepcopy(asteroid_map)
            if item == '#':

                mark_blind_spots(c, r, copy)
                count = count_asteroids(copy)

                if count > max_visible:
                    max_visible = count
                    max_location = (c,r)


    print(max_location, ":", max_visible)
    

if __name__ == "__main__":
    main()
