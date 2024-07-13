# 사과나무 (다이아몬드)

import sys
sys.stdin = open("input.txt","rt")

n = int(input())
apple = [list(map(int,input().split())) for _ in range(n)]

# 답안
res = 0
s=e=n//2
for i in range(n):
    for j in range(s,e+1): # s부터 e까지 도는 for문
        res += apple[i][j]
    if(i<n//2):
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)

# 내 답안 - 맞춤 !
m = n//2
sum = 0
for i in range(n): # apple[j][i]로 보고 함
    for j in range(n):
        c = abs(m-i)
        if(c<=j<=(n-1-c)):
            sum += apple[j][i]

print(sum)