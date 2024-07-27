import sys
# sys.stdin = open("input.txt","rt")
from collections import deque

n,m = map(int,input().split())
w = list(map(int,input().split()))
w.sort()
''' 답안은 w = deque(w) 이렇게 큐를 사용함'''
cnt = 0
while w:
    ''' 답안은 조건문 하나를 그냥 더 추가함
    if len(w)==1:
        cnt += 1
        break
    '''
    if len(w) > 1 and w[0]+w[-1] <= m:
        w.pop()
        w.pop(0) 
        ''' pop(0)은 앞으로 당기는 연산을 하기 때문에 굉장히 비효율적
        대신 deque 자료구조는 자료가 이동하지 않고 포인터 변수가 이동하기 때문에
        훨씬 효율적임 !
        w.popleft() 이렇게 하면 더 효율적임'''
        cnt += 1
    else:
        w.pop()
        cnt += 1

print(cnt)