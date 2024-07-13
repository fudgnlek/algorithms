# K번째 큰 수

import sys
# sys.stdin = open("input.txt","rt")

n,k = map(int,input().split())
num = list(map(int,input().split()))

# 조합 사용
from itertools import combinations
add = []
for i in combinations(num,3):
    a = i[0]+i[1]+i[2]
    add.append(a)

# 내림차순 정렬
add.sort(reverse=True)

# 리스트에서 중복 제거
# set 이용 (set은 중복이 불가능하니까)
add2 = set(add)
add2 = list(add2)
add2.sort(reverse=True)
#print(add2)

# for문 이용
# result = []
# for i in add:
#     if i not in result:
#         result.append(i)
# print(result)

print(add2[k-1])

# # 답안 (3중 for문 이용)
# res = set()
# for i in range(n):
#     for j in range(i+1,n):
#         for m in range(j+1,n):
#             res.add(num[i]+num[j]+num[m])
# res = list(res) # set은 정렬 기능이 없어서 list로 바꿔줌
# res.sort(reverse=True)
# print(res[k-1])