# 가장 높은 탑 쌓기
import sys
# sys.stdin=open("input.txt","r")
input=sys.stdin.readline

n=int(input())
arr=[list(map(int,input().split()))for _ in range(n)]
arr.sort(key = lambda x : x[0],reverse=True)
# print(arr)

dp=[0]*n

for i in range(n):
    dp[i]=arr[i][1]
    for j in range(i):
        if arr[i][2]<arr[j][2]:
            dp[i]=max(dp[i],dp[j]+arr[i][1])
print(max(dp))
