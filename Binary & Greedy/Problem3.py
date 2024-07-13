# 뮤직비디오 (결정알고리즘)

import sys
sys.stdin = open("input.txt","rt")

n,m = map(int,input().split())
a = list(map(int,input().split()))

# 내 답안 - 1번빼고 맞음 (Check 함수 답이랑 똑같음 !! ㅎㅎ)
# 답안대로 고치니까 (While문) 1번 해결됨
def Check(mid):
    cnt = 1
    sum = 0
    for i in range(n):
        if(sum+a[i]>mid):
            # sum에 한 곡을 넣는다는 것 자체가 dvd의 용량은 적어도 노래 중 가장 긴 노래보다 커야함 (이게 반례였음)
            sum=a[i]
            cnt+=1
        else:
            sum+=a[i]
    return cnt

lt = 1
rt = sum(a)
res = 0
maxx = max(a) # 가장 긴 노래 찾아줌

while(lt<=rt):
    mid = (lt+rt)//2
    # m보다 작은 경우에도 답이 될수는 있음 2개에 담기는건 무조건 3개에도 담길테니까 (답안)
    # mid가 제일 긴 노래보다 커야하는 조건 추가 (반례 수정 부분)
    if mid>=maxx and (Check(mid)<=m):
        res=mid
        rt=mid-1
    else:
        lt=mid+1

print(res)