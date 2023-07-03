# 격자판 최대합

import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)] # 2차원 리스트 형태로 입력받음

'''# 답안
largest = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1+=arr[i][j]
        sum2+=arr[j][i]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2

sum1=sum2=0
for i in range(n):
    sum1+=arr[i][i]
    sum2+=arr[i][n-i-1]
if sum1>largest:
        largest=sum1
if sum2>largest:
    largest=sum2

print(largest) '''

# 내 답안 - 틀렸다가 수정 완료 (답안이랑 다른거 거의 없음...)
m = 0 # 최댓값
sum3 = 0 
sum4 = 0
for i in range(n):
    sum1 = 0
    sum2 = 0
    sum3 += arr[i][i] # 대각선 1
    sum4 += arr[i][n-i-1] # 대각선 2
    for j in range(n):
        sum1 += arr[i][j] # 각 행
        sum2 += arr[j][i] # 각 열
    if(m<sum1):
        m=sum1
    elif(m<sum2):
        m=sum2
if(m<sum3):
    m=sum3
elif(m<sum4):
    m=sum4

print(m)