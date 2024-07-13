import sys
from itertools import combinations
# sys.stdin = open("input.txt","rt")

n,k = map(int,input().split())
a=list(map(int,input().split()))
# 내 답안 (itertools 사용)
# num = list(map(int,input().split()))
# tmp = []

# for a in combinations(num,3):
#     tmp.append(sum(a))

# tmp = set(tmp)
# tmp = list(tmp)
# tmp.sort(reverse=True)

# print(tmp[k-1])

# 조합 사용하는거 itertools 구글링함
# 결과값 구할 땐 중복 제거해야되는 부분 문제에서 파악 바로 못함
# set으로 중복 제거해줘야 하는거 강의 보고 알게 됨

# 강의 들으면서 조합 구현 부분 다시 듣기
# 조합 구현 및 전체 답안 코드 다시 복습 필요
res = set()
# 중복을 방지하기 위해 i+1, j+1 부터 각각 시작
for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            res.add(a[i]+a[j]+a[m])
res = list(res)
res.sort(reverse=True)
print(res[k-1])
