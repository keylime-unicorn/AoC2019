import sys

s = 0
for line in sys.stdin:
    i = int(line.strip())

    total = 0

    while i > 0:
        i = int(i/3)
        i = i-2

        if i >= 0:
            total += i
            print("total: ", total)

    s += total

print("sum: ", s)
