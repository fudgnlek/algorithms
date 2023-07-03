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


# Feedback     
# 무거운 것, 넓이 큰 것 먼저 쌓아야해서 내림차순 정렬하고 대소비교    
# -> 위에 올라가는 것이 더 가벼워야함     
