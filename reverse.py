import sys
test = int(sys.stdin.readline())
while(test > 0):
    test -= 1
    f,s = sys.stdin.readline().split()
    f = f[::-1]
    s = s[::-1]
    summ = int(f) + int(s)
    summ = str(summ)
    summ = int(summ[::-1])
    print(summ)
