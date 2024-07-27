import sys
from collections import deque
# sys.stdin = open('input.txt',"rt")

n,m = map(int,input().split())
risk = list(map(int,input().split()))
risk = deque(risk)
a = deque()
for i in range(n):
    a.append((i,risk[i]))
# 답안은 이렇게 함 (내가 a에 인덱스랑 값 같이 넣어서 큐로 만든거랑 같은 구현)
q = [(pos,val) for pos,val in enumerate(list(map(int,input().split())))]
q = deque(q)

cnt = 0 # 진료 횟수
while a:
    idx , p = a.popleft()
    '''
    # 답안은 나처럼 risk 안두고 if any 사용
    if any(p<x[1] for x in a):
        q.append((idx,p))
    any 함수는 조건이 참이 되면 그 순간 멈춤 (for문 다 도는게 아님)
    '''
    risk.popleft()
    if p < max(risk):
        a.append((idx,p))
        risk.append(p)
    else:
        cnt += 1
        if idx == m:
            print(cnt)
            break


