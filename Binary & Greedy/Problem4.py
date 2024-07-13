# 마구간 정하기 (결정알고리즘)

import sys
sys.stdin = open("input.txt","rt")

n,c = map(int,input().split())
a = []
for i in range(n):
    a.append(int(input()))

# 답안 (함수 부분 아예 못품)
def Check(mid):
    cnt = 1
    ep = a[0] # 첫번째 마구간에 말 배치
    for i in range(1,n):
        # 지금 현재 말을 배치하려고 하는 곳(a[i])과 그 전 말을 배치한 곳의 차이가 mid보다 크거나 같다면 배치 가능
        if a[i]-ep >= mid:
            cnt+=1
            # 배치해주고 ep를 현재 말을 배치한 곳으로 바꿔줌
            ep = a[i]
    return cnt

a.sort()

lt = 1 # 최소 거리
rt = a[n-1] # 답안 참고 (마구간 맨끝 좌표)
res = 0

while(lt<=rt):
    mid = (lt+rt)//2
    if(Check(mid)<c):
        rt=mid-1
    else:
        res=mid
        lt=mid+1

print(res)