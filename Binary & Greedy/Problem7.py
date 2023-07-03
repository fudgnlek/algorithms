# 창고정리

import sys
# sys.stdin = open("input.txt","rt")

l = int(input())
a = list(map(int,input().split()))
m = int(input())

# 내 답안 - 맞춤 ! (답안과 동일 - 오름차순 내림차순만 다름)
a.sort(reverse=True)

for _ in range(m):
    a[0]-=1
    a[l-1]+=1
    a.sort(reverse=True)

print(a[0]-a[l-1])