# 미로의 최단거리 통로 (BFS)

import sys
from collections import deque
# sys.stdin = open("input.txt","rt")
dx=[-1,0,1,0]
dy=[0,1,0,-1]
a=[list(map(int,input().split()))for _ in range(7)]

'''# 답안 - 비슷한데 내 답안보다 훨씬 간단한 느낌 !
Q=deque()
Q.append((0,0))
while Q:
    tmp=Q.popleft()
    for i in range(4):
        x=tmp[0]+dx[i]
        y=tmp[1]+dy[i]
        # 굳이 테두리 안만들고 이렇게 범위 설정해줌
        if 0<=x<=6 and 0<=y<=6 and a[x][y]==0:
            a[x][y]=1 # 체크 효과 (중복 예방)
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            Q.append((x,y))
# 그대로 값이 0이라면 벽에 막혀서 도착지에 못왔다는 말이니까 -1 출력
if dis[6][6]==0:
    print(-1)
else:
    print(dis[6][6])'''


# 내 답안 - 맞춤 !
# 가장자리를 0으로 초기화해줘야함
a.insert(0,[1]*7) # 0번 행에다가 모든 값이 0인 일차원 리스트를 insert
a.append([1]*7) # 맨 밑에다가 모든 값이 0인 일차원 리스트를 append
# 각 행의 오른쪽 왼쪽에도 0을 추가해주기
for x in a:
    # x가 a의 행을 말함
    x.insert(0,1) # 맨 앞
    x.append(1) # 맨 뒤

ch=[[0]*8 for _ in range(8)] # 온 길로 다시 돌아갈 필요 없으니까
ch[1][1]=1
dis=[[0]*8 for _ in range(8)]

dq=deque()
dq.append((1,1))

while True:
    if len(dq)==0:
        print(-1)
        break
    tmp=dq.popleft()
    if tmp[0]==7 and tmp[1]==7:
        print(dis[tmp[0]][tmp[1]])
        break
    for i in range(4):
        x=tmp[0]+dx[i]
        y=tmp[1]+dy[i]
        if a[x][y]==0 and ch[x][y]==0: 
            dq.append((x,y))
            ch[x][y]=1
            dis[x][y]=dis[tmp[0]][tmp[1]]+1

