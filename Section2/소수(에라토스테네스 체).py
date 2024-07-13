import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
'''
내 원래 답안 (주어진 수가 5 이상일거라고 잘못 생각, 시간 초과 발생)
res = 3 # 2,3,5
for x in range(6,n+1):
    if x%2==0 or x%3==0 or x%5==0:
        continue
    for j in range(6,x):
        if x%j==0:
            break
    else: res+=1 # 소수
print(res)
'''

# 강의 참고
# ch배열 생성해서 각 수의 배수를 쫙 제거해나가는 형식으로 진행
ch = [0]*(n+1)
res = 0
for i in range(2,n+1):
    if ch[i]==0: # 소수임
        res+=1
        for j in range(1,n+1):
            tmp = i*j
            if tmp > n:
                break
            ch[i*j]=1
        # 답안은 좀 더 간단
        # for j in range(i,n+1,i):
        #     ch[j]=1
print(res)