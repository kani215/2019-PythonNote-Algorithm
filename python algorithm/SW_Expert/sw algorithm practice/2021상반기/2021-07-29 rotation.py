MAIN_LIST = [0]*10
COUNT_LIST = [5,5,5,5,5] # not -
SUM_LIST = [0] * 10
def count_check():
    check = 0
    for i in COUNT_LIST:
        if i < 0 :
            check = 1
    if check == 1:
        print('-1')
    else:
        print(25-sum(COUNT_LIST))

def table_check(start,idx):
    sum1 = int()
    for i in range(start):
        sum1 += sum(MAIN_LIST[idx:idx+start])
    if sum1 == start**2:
        for j in range(start):
            SUM_LIST[idx+j] -= 1
            COUNT_LIST[start-1] -= 1
        
# input 
MAIN_LIST = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
[0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# for i in range(10):
#     MAIN_LIST[i] = map(int,input().split())
# main
for i in range(10):
    SUM_LIST[i] = sum(MAIN_LIST[i])
buliet = list(set(SUM_LIST)).sort()

while buliet:
    start = buliet.pop()
    for idx in range(10):
        if SUM_LIST[idx] == buliet:
            table_check()
            print(SUM_LIST)