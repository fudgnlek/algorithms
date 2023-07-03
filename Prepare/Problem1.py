# K번째 약수

import sys
#sys.stdin=open("input.txt","rt")

n,k = map(int,input().split())
# 여기서 int는 내장함수 !
# input.txt 내용같이 띄어쓰기로 되어있는 형식은 map()으로 읽어야함 


# 약수 구하기
dirtn = []
for i in range(1,n+1):
    if(n%i==0):
        dirtn.append(i)

#print(dirtn)

# K번째로 작은 수 출력
if(len(dirtn)<k):
    print(-1)
else:
    print(dirtn[k-1])


# # 답안 (list 안만드네...)
# cnt = 0
# # for ~ else 구문 : for문이 정상적으로 끝나면 else구문 실행하고 for문에서 break로 끝나버리면 else문 실행 안함
# for i in range(1,n+1):
#     if (n%i==0):
#         cnt+=1
#     if (cnt==k):
#         print(i)
#         break
# else:
#     print(-1)

