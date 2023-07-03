# 위상정렬 (그래프 정렬)
import sys
from collections import deque
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

n,m=map(int,input().split())
g=[[0]*(n+1) for _ in range(n+1)]
deg=[0]*(n+1)
dq=deque()

# 인접행렬 그래프
for i in range(1,n+1):
    a,b=map(int,input().split())
    g[a][b]=1
    deg[b]+=1

# 진입차수가 0인 수는 큐에 넣음
for i in range(1,n+1):
    if deg[i]==0:
        dq.append(i)

while dq:
    a=dq.popleft()
    print(a,end=' ')
    for i in range(1,n+1):
        if g[a][i]==1:
            deg[i]-=1
            if deg[i]==0:
                dq.append(i)


# Feedback
'''
< 위상정렬 >
어떤 일을 하는 "순서"를 찾는 알고리즘 (일의 선후관계를 유지하면서)
노드 입장에서 들어오는 간선 수 = 진입차수
진입차수를 값으로 하는 deg 배열을 생성해서 초기화는 0으로 진행

진입차수가 0이 되면 큐에 넣어줌
dq가 비면 끝나는 while문을 활용해서 popleft()해서 나온 수의 끝점(그래프) 의 deg-1 해주고
다시 해당 인덱스의 deg 값이 0이라면 dq.append 해줌
'''





