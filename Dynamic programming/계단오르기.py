# 도전과제 : 계단오르기 (Top-Down 방식)
import sys
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

def dfs(i):
    if i==1 or i==2:
        return i
    if dp[i]!=0:
        return dp[i]
    else:
        dp[i]=dfs(i-1)+dfs(i-2)
        return dp[i]

n=int(input())
dp=[0]*(n+1)
print(dfs(n))
