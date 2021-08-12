MAIN_LIST = [0] * 10
COUNT_LIST = [5,5,5,5,5] # not -
SUM_LIST = [0] * 10
# input 
MAIN_LIST = [
    [1,1,1,1,1  ,1,1,1,1,1],
    [1,1,1,1,1  ,1,1,1,1,1],
    [1,1,1,1,1  ,1,1,1,1,1],
    [1,1,1,1,1  ,1,1,1,1,1],
    [1,1,1,1,1  ,1,1,1,1,1],
    [1,1,1,1,1  ,1,1,1,1,1],
    [1,1,1,1,1  ,1,1,1,1,1],
    [1,1,1,1,1  ,1,1,1,1,1],
    [1,1,1,1,1  ,1,1,1,1,1],
    [1,1,1,1,1  ,1,1,1,1,1],
]
# for i in range(10):
#     MAIN_LIST[i] = list(map(int,input().split()))

def count_check():
    check = 0
    for i in COUNT_LIST:
        if i < 0 :
            check = 1
    if check == 1:
        print('-1')
    else:
        print(COUNT_LIST)
        print(25-sum(COUNT_LIST))

def table_check(idx, biggest_papper):
    for loc in range(10):
        if MAIN_LIST[idx][loc] == 1:
            sum_check = 0

            for mx in range(biggest_papper):
                sum_check += sum(MAIN_LIST[idx+mx][loc:loc + biggest_papper])
            if sum_check == biggest_papper**2:
                for mx in range(biggest_papper): 
                    SUM_LIST[idx+mx] -= biggest_papper
                    for my in range(biggest_papper):
                        MAIN_LIST[idx+mx][idx+my] -= 1
                COUNT_LIST[biggest_papper-1] -= 1
        else:
            continue


    
# main
for i in range(10):
    SUM_LIST[i] = sum(MAIN_LIST[i])
buliet = list(set(SUM_LIST))

while buliet:
    biggest_papper = buliet.pop()
    if biggest_papper < 1:
        break
    elif biggest_papper <= 5:
        for idx in range(10):
            if SUM_LIST[idx] >= biggest_papper:
                table_check(idx, biggest_papper)
                # print(biggest_papper,idx,SUM_LIST)
                # print(0,0,COUNT_LIST)

count_check()