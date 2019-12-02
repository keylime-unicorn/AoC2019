import sys

def calculate_mass():

    mass_sum = 0

    for line in sys.stdin:
        mass = int(line.strip()) // 3 - 2
        mass_sum += mass

    print(mass_sum)

def main():
    calculate_mass()

if __name__ == "__main__":
    main()
