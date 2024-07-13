# 소수 (에라토스테네스 체)

import sys
# sys.stdin = open("input.txt","rt")

n = int(input()) # 자연수 N

# 답안 - '에라토스테네스 체'라는 수학적 방법으로 프로그래밍 하는 것이 빠름 (소수를 구하는 여러가지 방법이 존재하지만)
ch = [0]*(n+1) # n+1 까지 해야 인덱스 번호가 20까지 생김
cnt = 0
for i in range(2,n+1):
    if(ch[i]==0):
        cnt += 1
        for j in range(i,n+1,i): # 마지막이 step, 즉 i만큼 커진다는 뜻 ! (i의 배수만 체크해야 하니까)
            ch[j] = 1
print(cnt)

# # 내 답안 - 동작은 되는데 큰 수가 들어오면 타임아웃 남 (쩨한 시간 1초라서 - 근데 1초가 아니더라도 시간 너무 오래걸리는듯)
# result = []

# for i in range(1,n+1):
#     cnt = 0 
#     for j in range(2,i):
#         if(i%j==0):
#             cnt = 1
#             break
#     if(cnt==0):
#         result.append(i)
# del result[0]
# print(len(result))
