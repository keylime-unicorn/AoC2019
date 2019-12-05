import sys

def check_digits(number):

    adjacent = False
    decrease = False

    number = str(number)

    #check adjacent digits are the same
    for i, _ in enumerate(number[:-1]):
        if number[i] == number[i+1]:
            adjacent = True
            break

    #check for never decreasing digits
    for i, _ in enumerate(number[:-1]):
        if int(number[i]) > int(number[i+1]):
            decrease = True
            break


    if adjacent and not decrease:
        return True
    else:
        return False

def main():
    line = sys.stdin.readline()
    start, stop = map(int, line.split("-"))

    total = 0    

    for number in range(start, stop+1):
        if check_digits(number):
            total += 1


    print(total)

if __name__ == "__main__":
    main()    
