# 수의 합

import sys
# sys.stdin = open("input.txt","rt")

n,ans = map(int,input().split())
arr = list(map(int,input().split()))

cnt = 0
l=0
r=1

# 답안
tot = arr[0]
while True:
    if tot<ans:
        if(r<n):
            tot+=arr[r]
            r+=1
        else:
            break
    elif tot==ans:
        cnt+=1
        tot -= arr[l]
        l+=1
    else:
        tot -= arr[l]
        l+=1
print(cnt)

'''# 내 답안 - 4,5번은 타임아웃남 (돌려보니까 답은 제대로 나오는데 시간이 오래걸려서 그런듯)
while(r<=n):
    tot = 0
    for i in range(l,r):
        tot += arr[i]
    if(tot<ans):
        r+=1
    elif(tot>ans):
        l+=1
    else:
        cnt+=1
        r+=1
        l+=1
print(cnt)'''