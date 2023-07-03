# 두 리스트 합치기

import sys
sys.stdin = open("input.txt","rt")

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

i = 0
j = 0
c = []

'''# 답안
while(i<n and j<m):
    if a[i]<=b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
if i<n:
    c = c+a[i:]
if j<m:
    c = c+b[j:]'''

# 내 답안 - 맞춤
for _ in range(n+m):
    if(a[i]<=b[j]):
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
    if(i==n):
        c = c+b[j:]
        break
    elif(j==m):
        c = c+a[i:]
        break

for x in c:
    print(x,end=' ')
