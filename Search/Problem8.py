# 곳감 (모래시계)

import sys
# sys.stdin = open("input.txst","rt")

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
m = int(input())

s=0
e=n-1
sum=0

# 답안
for i in range(m):
    h,t,k=map(int,input().split())
    if t==0: # 왼쪽
        for _ in range(k):
            # 0번째 자리 숫자를 pop하면 그 숫자가 저장되고 나머지 숫자는 자동으로 앞당겨짐
            arr[h-1].append(arr[h-1].pop(0)) # 그 숫자를 젤 뒤에다 append
    else: # 오른쪽
        for _ in range(k):
            arr[h-1].insert(0,arr[h-1].pop()) # 그냥 pop()하면 젤 뒤 숫자가 나옴 그걸 0번째 자리에 insert

for i in range(n):
    for j in range(s,e+1):
        sum+=arr[i][j]
    if(i>=n//2):
        s-=1
        e+=1
    else:
        s+=1
        e-=1

print(sum)

'''# 내 답안 - 맞춤 !
for i in range(m):
    num = list(map(int,input().split()))
    r = num[0]-1 # 몇번째 행
    for _ in range(num[2]): # 몇번 회전
        if(num[1]==0): # 왼쪽
            for j in range(n-1):
                arr[r][j],arr[r][j-1] = arr[r][j-1],arr[r][j]
        else: # 오른쪽
            for j in range(n-1,0,-1):
                arr[r][j],arr[r][j-1] = arr[r][j-1],arr[r][j]

for i in range(n):
    for j in range(s,e+1):
        sum+=arr[i][j]
    if(i>=n//2):
        s-=1
        e+=1
    else:
        s+=1
        e-=1

print(sum)'''