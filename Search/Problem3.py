# 카드 역배치 (정올 기출)

import sys
# sys.stdin = open("input.txt","rt")

# 답안
''' * (참고) swqp 방법
a,b=map(int,input().split())
print(a,b)
a,b=b,a
print(a,b) '''

a = list(range(21)) # 0-20까지 숫자 생성됨 (자동으로 리스트화됨)
for _ in range(10): # _하면 변수가 없는 것 (변수 대입하는 것도 시간 걸리니까 없으면 _하기)
    s,e = map(int,input().split())
    for i in range((e-s+1)//2): # 구간안에서 비교횟수 계산해보면 만약에 2-7이면 ((7-2)+1) //2 만큼 비교해야함
        a[s+i],a[e-i]=a[e-i],a[s+i] # swap
a.pop(0) # 0번 index 값을 pop (괄호 안에 아무것도 안적으면 맨 마지막 값이 pop)
for x in a:
    print(x,end=' ')

'''# 내 답안 - 해결 못함
num = []
for i in range(1,21):
    num.append(i)

for i in range(1):
    a,b=map(int,input().split())
    a=a-1
    new_num = num[a:b]
    del num[a:b]
    new_num.reverse()

지정한 구간에 해당하는 부분만 꺼내서 역순 시키고 다시 집어넣으려고 했는데
역순 시키는 것 까지는 했는데 그 리스트를 원래 리스트에 집어넣는 부분을 못함
리스트안에 리스트를 인덱스 지정해서 삽입하는게 안되나 ?
    num[a:b]=new_num # 이건 교체... 이렇게 하면 안됨

    print(num) '''
