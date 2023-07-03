# 응급실 (큐)

import sys
# sys.stdin = open("input.txt","rt")
from collections import deque

# 내 답안 - 맞춤 !
n,m = map(int,input().split())
risk = list(map(int,input().split()))
a = [] # 순서 인덱스와 값을 같이 저장
for i in range(n):
    a.append((i,risk[i]))

a = deque(a)
cnt = 0

while a:
    for i in range(1,len(a)):
        if a[0][1]<a[i][1]:
            temp = a.popleft()
            a.append(temp)
            break
    else:
        if a[0][0]==m:
            cnt+=1
            print(cnt)
            break
        else:
            a.popleft()
            cnt+=1