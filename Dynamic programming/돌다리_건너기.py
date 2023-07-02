# 도전과제 : 돌다리 건너기 (Bottom-Up)
import sys
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

n=int(input())
dp=[0]*(n+2)

dp[1],dp[2]=1,2
for i in range(3,n+2):
    dp[i]=dp[i-2]+dp[i-1]

print(dp[n+1])
