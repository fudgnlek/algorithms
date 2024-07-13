import sys
sys.stdin = open("input.txt","rt")

n, m = map(int, input().split())
a=[0]*(n+m+1)
for i in range(1,n+1):
    for j in range(1,m+1):
        tmp = i+j
        a[tmp]+=1
res = max(a)
for idx,x in enumerate(a):
    if x == res:
        print(idx,end=' ')
