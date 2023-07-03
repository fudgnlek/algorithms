# 정다면체

import sys
# sys.stdin = open("input.txt","rt")

n,m = map(int,input().split())

# # 답안
# cnt = [0]*(n+m+3) # 크기 넉넉하게 잡기 위해 +3 (모두 0으로 초기화)
# max = 0 # -2147000000 (최솟값)
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         cnt[i+j]+=1 # 숫자 별로 몇번 등장하는지 기록
# for i in range(n+m+1):
#     if(cnt[i]>max):
#         max = cnt[i]
# for i in range(n+m+1):
#     if(cnt[i]==max):
#         print(i, end=" ")

# 내가 푼 것 (완벽하게 나 혼자서는 못품 - 답안 참고)
# 던져서 나올 수 있는 눈의 합 구하기
sumList = []
for i in range(1,n+1):
    for j in range(1,m+1):
        sum = i+j
        sumList.append(sum)

# 나올 확률이 높은 것이 몇번인지 구하기
cnt = sumList.count(2)
result = []
for i in range(3,n+m+1):
    temp = sumList.count(i)
    if(cnt < temp):
        cnt = temp

# 높은 것이 나오는 수 모두 구하기 (답안 참고해서 품)
for i in range(2,n+m+1):
    s = sumList.count(i)
    if(s==cnt):
        print(i,end=" ")

