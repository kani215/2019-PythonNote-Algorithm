import sys

N = int(input())
dust_mid = [0] * N

for idx in range(N):
    dust_mid[idx] = [0,0]+list(map(int, input().split()))+[0,0]
start = ((N//2)+2, (N//2)+2)
dust = [[0]*(N+4)]*2 + dust_mid + [[0]*(N+4)]*2

dx = [0,1,0,-1]
dy = [-1,0,1,0]
# repeat1 = [0,1,2,2,3,3,0,0] #8 1*2+2*3
# repeat2 = [0,1,2,2,3,3,0,0,0,1,1,1,2,2,2,2,3,3,3,3,0,0,0,0] #24 1*2+2*2+3*2+4*3 
# repeat3 = [0,1,2,2,3,3,0,0,0,1,1,1,2,2,2,3,3,3,0,0,0,0,] #48 1*2+2*2+3*2+4*2+5*2+6*3
# 5, 9, 13
repeat = list()
for change_dir, rule in enumerate(range(4*(N//2)+1)):
    rule = rule//2 +1
    for _ in range(rule):
        repeat.append(change_dir%4)

for dust_dirct in repeat:
    x, y = start
    now = dust[x + dx[dust_dirct]][y + dy[dust_dirct]]
    dust[x+ dx[dust_dirct]*3][y + dy[dust_dirct]*3] += int(0.05*now)
    dust[x+ dx[dust_dirct]*2+dx[(dust_dirct+1)%4]][y + dy[dust_dirct]*2+dy[(dust_dirct+1)%4]] += int(0.1*now)
    dust[x+ dx[dust_dirct]*2+dx[(dust_dirct+3)%4]][y + dy[dust_dirct]*2+dy[(dust_dirct+3)%4]] += int(0.1*now)
    dust[x + dx[dust_dirct]*1+dx[(dust_dirct+1)%4]][y + dy[dust_dirct]*1+dy[(dust_dirct+1)%4]] += int(0.07*now)
    dust[x + dx[dust_dirct]*1+dx[(dust_dirct+3)%4]][y + dy[dust_dirct]*1+dy[(dust_dirct+3)%4]] += int(0.07*now)
    dust[x + dx[dust_dirct]*1+dx[(dust_dirct+1)%4]*2][y + dy[dust_dirct]*1+dy[(dust_dirct+1)%4]*2] += int(0.02*now)
    dust[x + dx[dust_dirct]*1+dx[(dust_dirct+3)%4]*2][y + dy[dust_dirct]*1+dy[(dust_dirct+3)%4]*2] += int(0.02*now)
    dust[x + dx[(dust_dirct+1)%4]][y + dy[(dust_dirct+1)%4]] += int(0.01*now)
    dust[x + dx[(dust_dirct+3)%4]][y + dy[(dust_dirct+3)%4]] += int(0.01*now)
    dust[x + dx[dust_dirct]*2][y + dy[dust_dirct]*2] += (now-int(0.05*now)-int(0.1*now)*2-int(0.07*now)*2-int(0.02*now)*2-int(0.01*now)*2)

    dust[x + dx[dust_dirct]][y + dy[dust_dirct]] = 0
    start = (x + dx[dust_dirct], y + dy[dust_dirct])
    print(dust)

ans = int()
for x in range(N+4):
    ans += sum(dust[x])
print(ans)
for x in range(2,N+1):
    ans -= sum(dust[x][2:N+3])
print(ans)
