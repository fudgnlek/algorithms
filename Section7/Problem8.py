# 사과나무

# Section 2에 있던거랑 같은 문제인데 BFS로 품
# 가장 중심 좌표를 루트노드에 두고 시작 (상태노드 네가닥 - 상하좌우)
# 직접 해보면 알겠지만 레벨 순으로 탐색하면 다이아몬드 모양으로 탐색됨

# 답안 - 혼자 못품
import sys
from collections import deque
# sys.stdin = open("input.txt","rt")

# 시계방향으로 상하좌우 탐색
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n =int(input())
a=[list(map(int,input().split())) for _ in range(n)]
ch=[[0]*(n) for _ in range(n)] # 체크리스트도 이차원리스트로 생성
sum=0
ch[n//2][n//2]=1 # 시작점 (중심좌표)
sum+=a[n//2][n//2]
dq=deque()
dq.append((n//2,n//2))
L=0

while True:
    # 종착지점 (다이아몬드 모양으로 탐색이 끝난 경우)
    if L==n//2:
        break
    size=len(dq)
    # 큐안에 있는 노드 갯수만큼 for문 실행
    for i in range(size):
        tmp=dq.popleft()
        for j in range(4): # 시계방향으로 상하좌우 탐색
            x=tmp[0]+dx[j] # x값
            y=tmp[1]+dy[j] # y값
            if ch[x][y]==0:
                sum+=a[x][y]
                ch[x][y]=1
                dq.append((x,y))
    L+=1

print(sum)
