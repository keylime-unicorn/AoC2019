import sys


s = 0
for line in sys.stdin:
    i = int(line.strip())
    i = int(i/3)
    i = i-2
    s += i

print(s)
