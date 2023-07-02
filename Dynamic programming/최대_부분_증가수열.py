# 최대 부분 증가수열
import sys
# sys.stdin=open("input.txt","r")
input=sys.stdin.readline

# 강의 답
n=int(input())
a=list(map(int,input().split()))
a.insert(0,0)
dp=[0]*(n+1)
dp[1]=1
for i in range(2,n+1):
    maxx=0
    for j in range(i-1,0,-1):
        if a[j]<a[i] and dp[j]>maxx:
            maxx=dp[j]
    dp[i]=maxx+1

print(max(dp))

'''
# 내 답변 - 맞긴한데 강의 답이랑 다름
n=int(input())
a=list(map(int,input().split()))
dp=[1]*(n)

for i in range(n):
    for j in range(0,i):
        if a[i]>a[j]:
            dp[i]=max(dp[j]+1,dp[i])

print(max(dp))
'''
