# 랜선 자르기 (결정알고리즘)

import sys
# sys.stdin = open("input.txt","rt")

k,n = map(int,input().split())
a = []

# 내 답안 + 강의 참고
# 참고한 부분 : rt 잡는 거, while문에 elif부분 (이분검색이 끝날때까지 수행, res둬서 조건을 만족한다면 일단 답으로 지정)

# 함수에서 a 배열은 인자로 안보내줘도 되는거 제대로 이해하기 !
def Check(mid):
    temp = 0
    for i in range(k):
        temp += a[i]//mid
    return temp

# largest = 0
for _ in range(k):
    a.append(int(input()))
    # 답안에서 rt 잡은 부분
    '''tmp = int(input())
    a.append(tmp)
    largest = max(largest,tmp)'''

a.sort()

lt=1
rt=a[k-1] # 원래 랜선 중 가장 긴 랜선 길이를 최댓값으로 둠
res = 0 # 답

while(lt<=rt):
    mid=(lt+rt)//2
    if(Check(mid)<n):
        rt=mid-1
    else:
        res=mid
        lt=mid+1
print(res)
