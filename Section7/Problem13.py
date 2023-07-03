# 섬나라 아일랜드 (BFS 활용)

import sys
from collections import deque
# sys.stdin = open("input.txt","rt")

# 내 답안 (답안 참고)
n=int(input())
# 대각선, 상하좌우까지
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
p=[list(map(int,input().split())) for _ in range(n)]
dq = deque()
cnt=0

for i in range(n):
    for j in range(n):
        if p[i][j]==1:
            dq.append((i,j))
            p[i][j]=0 
            while dq: # for문 안에 while문 넣어서 dq가 빌때 cnt+1 해줌 (이 부분을 해결 못함 전체적인 코드는 직접 작성함)
                tmp=dq.popleft()
                for k in range(8):
                    x=tmp[0]+dx[k]
                    y=tmp[1]+dy[k]
                    if 0<=x<=n-1 and 0<=y<=n-1 and p[x][y]==1:
                        p[x][y]=0
                        dq.append((x,y))
            cnt+=1
print(cnt)