import sys

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def check_digits(number):

    double = False
    decrease = False

    number = str(number)

    #check adjacent digits are the same
    num_digits = {}
    for d in digits:
        num_digits[d] = 0

    for i in number:
        num_digits[i] += 1

    for d in digits:
        if num_digits[d] == 2:
            double = True

    #check for never decreasing digits
    for i, _ in enumerate(number[:-1]):
        if int(number[i]) > int(number[i+1]):
            decrease = True
            break

    if double and not decrease:
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
