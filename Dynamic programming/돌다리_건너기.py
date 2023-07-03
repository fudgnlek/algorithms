# 도전과제 : 돌다리 건너기 (Bottom-Up)
import sys
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

n=int(input())
dp=[0]*(n+2)

dp[1],dp[2]=1,2
for i in range(3,n+2):
    dp[i]=dp[i-2]+dp[i-1]

print(dp[n+1])

# 만약 중간에 돌다리 디디지 못한다는 전제조건이 추가된다면  
# 딛지 못하는 부분을 0으로 두고 진행하면 됨  
