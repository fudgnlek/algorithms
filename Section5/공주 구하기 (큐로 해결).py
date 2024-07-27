import sys
from collections import deque
# sys.stdin = open("input.txt","rt")

n,k = map(int,input().split())
a = []
for i in range(n):
    a.append(i+1)
a = deque(a)
# 답안
dq = list(range(1,n+1))
dq = deque(dq)

'''
while문에서 for문 구현 자체를 생각 못함
'''
while len(dq)>1:
    for _ in range(k-1):
        tmp = dq.popleft()
        dq.append(tmp)
    dq.popleft() # k번째 왕자 제거

'''
답안은 while dq: 해서
if len(dq)==1:
    print(dq[0])
    dq.popleft()
이렇게 구현함
'''
print(dq[0])