# 5shortest way algorithm
# find start
# fu.cking memory = use stack

V, E = map(int,input().split())
start = int(input())
datamemo =[[] for _ in range(V+1)] 
stack = []
start_dis = [0]*(V+1)

for _ in range(E):
    x,y,w = map(int, input().split())
    datamemo[x].append((y,w))
    if x == start:
        stack.append(y)
        if start_dis[y] != 0:
            start_dis[y] = min(w, start_dis[y])
        else :
            start_dis[y] = w
# roll stack to find shortest way 
while len(stack) != 0:
    now_node = stack.pop() 
    for next_node, w in datamemo[now_node]:
        if start_dis[next_node] != 0:
            start_dis[next_node] = min(start_dis[next_node], start_dis[now_node] + w)
        else :
            start_dis[next_node] = start_dis[now_node] + w
        stack.append(next_node)

# print
for i in range(1,V+1):
    if start == i :
        print(0)
    elif start_dis[i] == 0:
        print("INF")
    else :
        print(start_dis[i])