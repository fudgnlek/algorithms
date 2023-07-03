# 역수열 (그리디)

import sys
sys.stdin = open("input.txt","rt")  

n = int(input())
a = list(map(int,input().split()))

'''# 답안 - 내 답안과 다른 방식
a.insert(0,0) # 0번째를 0으로 초기화하고 1부터 하는걸로도 가능함
seq = [0]*n
for i in range(1,n+1):
    for j in range(n):
        if a[i]==0 and seq[j]==0: # 자기 자리 찾아간 경우
            seq[j]=i
            break
        elif seq[j]==0: # 빈자리인 경우
            a[i]-=1 # 앞에 큰숫자가 있는 개수를 -1 해줌 0이 되면 그때 해당하는 j가 해당 숫자의 자리
for x in seq:
    print(x,end=' ')'''

# 내 답안 - 맞춤 !
b = [0]*n
cnt = 0

for i in range(n):
    for j in range(n):
        if b[j]==0:
            cnt+=1
        if cnt==(a[i]+1):
            b[j]=i+1
            cnt=0
            break
for x in b:
    print(x,end=' ')