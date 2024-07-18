import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

row = 0
col = 0
cross1 = 0
cross2 = 0

for i in range(n):
    tmp = sum(arr[i])
    if row < tmp: # 각 행의 최댓값
        row = tmp
    cross1 += arr[i][i]
    cross2 += arr[i][n-1-i]
    cross = max(cross1,cross2) # 두 대각선의 합 중 최댓값

    tmp2 = 0 
    for j in range(n):
        tmp2 += arr[j][i]
    if col < tmp2: # 각 열의 최댓값
        col = tmp2

print(max(row,col,cross))

'''
답안은 행과 열을 이중포문 돌려서 같이 구했고 최댓값도 하나만 구함
그리고 대각선은 새로 포문돌려서 최댓값 구함
대충 비슷한듯
'''