# 알리바바와 40인의 도둑 (Bottom-Up)
import sys
# sys.stdin=open("input.txt","r")
input=sys.stdin.readline

# 강의 설명 듣고난 후 코드 작성 (맞음)
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*n for _ in range(n)]

# 0행 0열 초기화   
# 0행 0열은 어차피 경로 하나라서 쭉 누적하면 됨 (그 값으로 초기화)  
for i in range(n):
    dp[0][i]=a[0][i]+dp[0][i-1]
    dp[i][0]=a[i][0]+dp[i-1][0]

for i in range(1,n):
    for j in range(1,n):
        dp[i][j]=min(dp[i-1][j],dp[i][j-1])+a[i][j]
# print(dp)
print(dp[n-1][n-1])

# (도착지점 입장에서 보면 위나 왼쪽에서 올 수 있음)    


# 알리바바와 40인의 도둑 (Top-Down)
import sys
# sys.stdin=open("input.txt","r")
input=sys.stdin.readline

def dfs(i,j):
    # 메모이제이션 (0이 아니라면 굳이 더 dfs 진행하지 않음)
    if dp[i][j]!=0:
        return dp[i][j]
    if i==j==0:
        return a[0][0]
    else:
        if j==0: # 0행 초기화
            dp[i][j]= dfs(i-1,j)+a[i][j]
        elif i==0: # 0열 초기화
            dp[i][j]= dfs(i,j-1)+a[i][j]
        else: # 아닌 경우 최솟값 찾아서 +a[i][j]
            dp[i][j]= min(dfs(i-1,j),dfs(i,j-1))+a[i][j]
    return dp[i][j]

n=int(input())
a=[list(map(int,input().split()))for _ in range(n)]
dp=[[0]*n for _ in range(n)]
print(dfs(n-1,n-1))

# Feedback    
# 코드 작성도 스스로 못함  
# 끝 (n-1,n-1) 부터 시작   


















