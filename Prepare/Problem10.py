# 점수계산

import sys
sys.stdin = open("input.txt","rt")

n = int(input())
num = list(map(int,input().split()))

# 내 답안 - 맞춤 !
a,grade = 1,0
for i in range(len(num)):
    if(num[i]==1):
        grade += a
        a += 1
    else:
        a = 1

# # 답안 - if문 순서만 다름 
# a=0
# grade=0
# for x in num:
#     if x==1:
#         a+=1
#         grade+=a
#     else:
#         a=0

print(grade)