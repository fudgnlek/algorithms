import sys
from collections import deque
sys.stdin = open("input.txt","rt")

# 내 답안도 맞긴 함
a = input()
n = int(input())
for i in range(n):
    cl = deque(input())
    res = []
    while cl:
        tmp = cl.popleft()
        if tmp in a:
            if tmp not in res:
                res.append(tmp)
        if res==a:
            print("#%d YES" %(i+1))
            break
    if res!=a:
        print("#%d NO" %(i+1))
''' 답안
for i in range(n):
    plan = input()
    dq = deque(a)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))
'''