# 공주구하기 (큐)

import sys
# sys.stdin = open("input.txt","rt")
from collections import deque

# 내 답안 + 답안 참고
n,k = map(int,input().split())
q = list(range(1,n+1)) # 리스트 생성
q = deque(q)

while q:
    for _ in range(k-1):
        a = q.popleft()
        q.append(a)
    q.popleft()
    if(len(q)==1):
        print(q[0])
        q.popleft() # 끝


