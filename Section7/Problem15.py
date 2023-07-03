# 토마토 (BFS 활용)

import sys
from collections import deque
sys.stdin = open("input.txt","rt")
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 답안 참고 - 혼자 못품 (day 배열 사용하는거 생각못함)
# 5초 채점기 안돌아가서 채점기로는 확인 못함 (따로 확인해서 다 맞은거 확인함)
m,n=map(int,input().split())
t=[list(map(int,input().split()))for _ in range(n)]
dq=deque()
cnt=0
day = [[0]*m for _ in range(n)] # 답안 참고 (날짜 표현을 위해 사용)
maxx = 0 # 출력될 값

# 익은 토마토 위치 큐에 모두 append
for i in range(n):
    for j in range(m):
        if t[i][j]==1:
            dq.append((i,j))

while dq:
    tmp=dq.popleft()
    for k in range(4):
        x=tmp[0]+dx[k]
        y=tmp[1]+dy[k]
        if 0<=x<=n-1 and 0<=y<=m-1 and t[x][y]==0:
            t[x][y]=1
            dq.append((x,y))
            day[x][y]=day[tmp[0]][tmp[1]]+1

flag=1
# 토마토가 모두 익지 못하는 상황이라면 -1 출력
for i in range(n):
    for j in range(m):
        if t[i][j]==0:
            flag=0
if flag==1:
    # day 배열에서 가장 큰 값이 모두 익을 때까지의 최소 날짜
    for i in range(n):
        for j in range(m):
            if maxx<day[i][j]:
                maxx=day[i][j]
    print(maxx)
else:
    print(-1)