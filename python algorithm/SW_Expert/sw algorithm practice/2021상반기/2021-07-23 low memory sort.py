import sys

heap = list()
N = int(sys.stdin.readline())
li = [0]*10001
for _ in range(N):
    li[int(sys.stdin.readline())] += 1

for i in range(10001):
    if li[i] != 0:
        for _ in range(li[i]):
            sys.stdout.write(str(i)+'\n')

