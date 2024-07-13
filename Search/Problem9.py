# 봉우리

import sys
sys.stdin = open("input.txt","rt")

# 외워두기
dx = [-1,0,1,0] # 행 
dy = [0,1,0,-1] # 열

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

# 가장자리를 0으로 초기화해줘야함
a.insert(0,[0]*n) # 0번 행에다가 모든 값이 0인 일차원 리스트를 insert
a.append([0]*n) # 맨 밑에다가 모든 값이 0인 일차원 리스트를 append
# 각 행의 오른쪽 왼쪽에도 0을 추가해주기
for x in a:
    # x가 a의 행을 말함
    x.insert(0,0) # 맨 앞
    x.append(0) # 맨 뒤

cnt = 0 
# 1부터 돌아야함 0번째는 0으로 모두 초기화되어있기때문에
for i in range(1,n+1):
    for j in range(1,n+1):
        # k가 0부터 3까지 돈다 (상하좌우 확인)
        # 파이썬에는 all 함수 존재 (괄호안의 모든것이 참이어야 참)
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1

print(cnt)

'''# 내 답안 - 미해결
arr = []
for i in range(n):
    for j in range(n):
        main = num[i][j] # 확인대상

        # 가장자리는 0
        if(i==0):
            up=0
            down = num[i+1][j]
            if(j==0):
                left=0
                right = num[i][j+1]
            elif(j==n-1):
                right=0
                left = num[i][j-1]
        
        if(i==n-1):
            down=0
            up = num[i-1][j]
            if(j==0):
                left=0
                right = num[i][j+1]
            elif(j==n-1):
                right=0
                left = num[i][j-1]

        # 봉우리인지 확인
        if(main>up and main>down and main>left and main>right):
            arr.append(main)

print(arr)
print(len(arr)) '''

