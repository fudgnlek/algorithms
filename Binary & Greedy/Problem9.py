# 증가수열 만들기 (그리디)

import sys
from collections import deque
sys.stdin = open("input.txt","rt")

n = int(input())
a = list(map(int,input().split()))
a = deque(a)
b = []

# 답안
# 내가 한것처럼 pop해주는게 아니라 포인터 이동으로 품 
# 일단 넣어주고 넣은걸 정렬해서 작은값을 res에 넣어주는 형식으로 해결 
lt = 0
rt = n-1
last = 0
res = ""
tmp = []
while(lt<=rt):
    # 일단 last값보다 크면 왼쪽 오른쪽 모두 넣어줌
    if a[lt]>last:
        tmp.append((a[lt],'L'))
    if a[rt]>last:
        tmp.append((a[rt],'R'))
    # 그리고 tmp 정렬 (lt,rt값에 의해 오름차순 정렬)
    tmp.sort()
    # 만약 tmp에 아무것도 들어오지 않았다면 끝 값 두개 모두 last값보다 작다는 뜻 - 종료(break)
    if len(tmp)==0:
        break
    # 뭔가 들어왔다면 그 중 첫번째 값의 1번 자료를 res에 넣어줌 (정렬 했으니 작은 값의 L또는R값이 들어갈 것)
    else:
        res = res + tmp[0][1]
        last = tmp[0][0] # last값은 첫번째 값의 0번 자료 (숫자)
        if tmp[0][1] == 'L':
            lt+=1
        else:
            rt-=1
    tmp.clear()
print(len(res))
print(res)

# 내 답안 - 맞춤 ! (근데 약간 노가다 느낌...)
temp = 0
while(a):
    if len(a)==1:
        if(temp<a[0]):
            b.append('L')
            break
        else:
            break
    if(temp<a[0] and temp<a[-1]):
        if(a[0]<a[-1]):
            temp=a[0]
            a.popleft()
            b.append('L')
        else:
            temp=a[-1]
            a.pop()
            b.append('R')
    elif(temp<a[0]):
        temp=a[0]
        a.popleft()
        b.append('L')
    elif(temp<a[-1]):
        temp=a[-1]
        a.pop()
        b.append('R')
    else:
        break

print(len(b))
for x in b:
    print(x,end='')