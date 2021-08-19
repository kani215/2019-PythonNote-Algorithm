N = 5
K = 8
A = [100, 99, 60, 80 ,30 ,20 ,10 ,89 ,99, 100]
# N,K = map(int,input().split())
# A = list(map(int,input().split()))
robot_loc = ['f'] * N
start = 1
while True:
    if robot_loc[-1] == 't':
      robot_loc[-1] = 'f' 
    #belt move
    robot_loc = list(robot_loc.pop()) + robot_loc
    A_s = []
    A_s.append(A.pop())
    A = A_s + A
    if robot_loc[-1] == 't':
        robot_loc[-1] = 'f' 


    # robot move
    check = []
    move = []
    for idx in range(N):
        if robot_loc[idx] == 't':
            check.append(idx)
    for _ in range(len(check)):
        loc = check.pop()
        if A[loc+1] >= 1 and robot_loc[loc+1] == 'f':
            A[loc+1]-=1
            move.append(loc)

    for loc in move:
        robot_loc[loc] = 'f' 
        robot_loc[loc+1] = 't'
    if robot_loc[-1] == 't':
        robot_loc[-1] = 'f' 

    #put robot
    if A[0] >= 1:
        robot_loc[0] = 't'
        A[0] -= 1

    #check stop
    cnt = 0
    for broke in A:
        if broke == 0:
            cnt +=1
    if cnt >= K:
        print(start)
        break
    start+=1    