# 침몰하는 타이타닉 (그리디)

import sys
from collections import deque
sys.stdin = open("input.txt",'rt')

n , m = map(int,input().split())
a = list(map(int,input().split()))

# 답안
a.sort()
a = deque(a) # a를 deque 자료형으로 변경
cnt = 0

# a 가 비면 반복문 끝남
while a:
    # 만약 마지막에 한 사람이 남는다면 두번째 if문에서 자기자신을 두번 더함 - 논리적 오류
    # 그리고 만약 자기자신을 두번 더한게 m을 넘지않아서 else문으로 간다면 
    # 자료는 하난데 두번 pop해서 오류 발생 그래서 길이가 하나라면 (사람이 한명 남았다면) 바로 구명보트 태워 보내고 while문 종료 (break)
    if len(a)==1:
        cnt+=1
        break
    # 가장 가벼운 사람과 무거운 사람을 더한게 리미트보다 크다면 가장 무거운 사람 혼자 타고 가야함
    # [-1]하면 가장 마지막 자료를 뜻함 (기억하기)
    if a[0]+a[-1]>m:
        # 가장 무거운 사람 (가장 끝에 있는 사람)을 pop시켜줌
        a.pop()
        cnt+=1
    else:
        '''# 리스트 자료형에서 pop연산은 계속 앞당겨져서 비효율적임 - deque 사용 !
        a.pop(0) # 가장 가벼운 사람 pop'''
        a.popleft() # deque 자료형 사용할때 맨 앞 자료 pop 시키는 것 (효율적)
        a.pop()
        cnt+=1
print(cnt)

'''# 내 답안 - 맞춤 !
a.sort(reverse=True)
cnt = 0
for i in range(n):
    if(a[i]!=1000):
        temp = m-a[i]
        for j in range(i+1,n):
            if(temp>=a[j]):
                a[j]=1000
                # 구명보트 2명까지만 탈 수 있음 (이게 틀린 부분)
                break
        a[i]=1000
        cnt+=1    
print(cnt) '''