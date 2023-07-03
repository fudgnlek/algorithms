# 송아지 찾기 (BFS)

# BFS : 넓이우선탐색 (레벨탐색) - 0레벨에서 한번만에 갈 수 있는 곳 1레벨을 다 보고 두번만에 가는 2레벨 다 보고 이런식으로 탐색
# 큐 사용 (FIFO) : 루트노드 값을 큐에 넣고 출발 (큐에 들어가면 탐색이라고 봐야함)
# 그 값이 pop되면 그 값에서 한번만에 갈 수 있는 노드값들 모두 큐에 들어감
# BFS는 최단거리 구할때 사용 ! (레벨 순으로 탐색하기 때문에 최초로 구해지는게 답)

import sys
from collections import deque
# sys.stdin = open("input.txt","rt")

# 답안 - 혼자 못품
MAX = 10000 # 문제에서 좌표의 맥시멈이 만
# 인덱스 번호가 좌표니까 +1 씩 해주기
ch=[0]*(MAX+1) # 중복 방지를 위한 checklist
dis=[0]*(MAX+1)
n,m = map(int,input().split()) # 출발점, 도착점
ch[n]=1 # 처음에 n에서 출발하니까 n은 check 
dis[n]=0 # 출발점이니까 0
dq=deque()
dq.append(n)

# 큐가 비어있으면 멈춤
while dq:
    now=dq.popleft()
    if now==m:
        break
    # 이렇게 해주면 next가 now-1,now+1,now+5 값이 되어 총 세바퀴를 돔
    for next in(now-1,now+1,now+5):
        if 0<next<=MAX: # 좌표값의 범위
            if ch[next]==0: # 방문 하지 않았을때만
                dq.append(next)
                ch[next]=1
                dis[next]=dis[now]+1 # 거리 값은 부모의 값에 +1하니까

print(dis[m])


