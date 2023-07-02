# 최대 선 연결하기
import sys
# sys.stdin=open("input.txt","r")
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
dp=[1]*(n)

for i in range(n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))


''' 내 답안인데 오류 존재 - 해결 못함
r=[0]*(n+1)
for idx,i in enumerate(arr):
    r[i]=idx
dp=[1]*(n+1)

for i in range(n):
    for j in range(i-1,0,-1):
        if r[j]<r[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(max(dp))'''
