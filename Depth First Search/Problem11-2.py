# 라이브러리를 이용한 조합 (수들의 조합)

# 라이브러리에 너무 의존하면 안됨 
# -> 코테 시험에 따라 라이브러리 사용을 제한하는 경우나 특정 조건을 만족하는 수만 뽑아라 등의 경우에는 라이브러리 사용 불가
import sys
import itertools as it
sys.stdin = open("input.txt","rt")

n,k = map(int,input().split())
a = list(map(int,input().split()))
m = int(input())
cnt=0
for x in it.combinations(a,k):
    if sum(x)%m==0:
        cnt+=1
print(cnt)