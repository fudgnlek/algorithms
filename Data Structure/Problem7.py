# 교육과정설계 (큐)

import sys
# sys.stdin = open("input.txt","rt")
from collections import deque
s = input()
n = int(input())

# 답안 - 혼자 못품
for i in range(n):
    plan = input()
    tmp = deque(s) # 다른 곳에 deque 한걸 저장해서 매번 초기화 되도록 해야 함
    for x in plan:
        if x in tmp:
            if x!=tmp.popleft(): # 순서 검사
                print("#%d NO" %(i+1))
                break
    else:
        if len(tmp)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))
