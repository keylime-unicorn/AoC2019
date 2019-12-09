import sys

direct_orbits = {}
indirect_orbits = {}


def get_indirect_orbits(obj):

    if obj == "COM":
        return 0
    
    return get_indirect_orbits(direct_orbits[obj]) + 1


def get_orbits():
        
    total = 0

    for obj in direct_orbits.keys():
        total += get_indirect_orbits(obj)
        
    return total


def main():

    for line in sys.stdin:
        orbitee, orbiter = line.split(")")
        orbiter = orbiter.strip()

        direct_orbits[orbiter] = orbitee

    print(get_orbits())
        

if __name__ == "__main__":
    main()
