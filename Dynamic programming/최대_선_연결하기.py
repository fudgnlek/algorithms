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

# Feedback 
# 네트워크 선, 돌다리 문제와 말만 다를 뿐이지 오른쪽 배열의 최대 부분 증가 수열 길이 구하면 됨   
# 왼쪽이 오름차순으로 증가수열이고 오른쪽과 선을 연결했을 때 겹치지 않으려면 오른쪽도 증가수열이어야 함   

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
