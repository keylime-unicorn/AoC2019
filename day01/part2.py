import sys

def calculate_mass(num):

    if num <= 0:
        return 0

    return calculate_mass(num // 3 - 2) + num

def main():
    
    total_mass = 0

    for line in sys.stdin:
        number = int(line.strip())
        total_mass += calculate_mass(number // 3 - 2)

    print(total_mass)

if __name__ == "__main__":
    main()
