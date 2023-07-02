# 네트워크 선 자르기 (Bottom-Up)
import sys
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

n=int(input())
dp=[0]*(n+1)
dp[1],dp[2]=1,2

for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[n])

# 네트워크 선 자르기 (Top-Down : 재귀, 메모이제이션)
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

n = int(input())
dp=[0]*(n+1)

print(dfs(n))
# print(dp)

'''
# 설명만 듣고 작성한 코드
# 결과값은 제대로 나오는데 생각해보니까 메모이제이션이 안된 코드인듯
def dfs(n):
    if dp[n]!=0:
        return dp[n]
    else:
        return dfs(n-1)+dfs(n-2)

n = int(input())
dp=[0]*(n+1)
dp[1],dp[2]=1,2

print(dfs(n))
'''
