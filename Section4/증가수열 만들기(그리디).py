import sys
# sys.stdin = open("input.txt","rt")
from collections import deque

n = int(input())
a = list(map(int,input().split()))
a = deque(a)
res = []

cnt = 0
tmp = 0
'''
답안 참고 - 내 답안도 정답이긴한데 너무 노가다 코드라서 참고하기
lt = 0
rt = n-1
answer = ""

while lt<=rt:
    if a[lt] > tmp:
        res.append((a[lt],'L'))
    if a[rt] > tmp:
        res.append((a[rt],'R'))
    res.sort() # 왼쪽 오른쪽 다 들어갔다면, 증가수열로 만들어야 하니까 정렬
    if len(res) == 0:
        break
    else:
        # 둘 다 들어간 경우 더 작은 값만 넣어줌
        # 인덱스 옮긴 후의 값과 비교했을 때의 상황도 고려해야하므로
        answer += res[0][1]
        tmp = res[0][0]
        if res[0][1] == 'L': # 왼쪽 끝
            lt += 1
        else: # 오른쪽 끝
            rt -= 1
    res.clear()

print(len(answer))
print(answer)
'''
while a:
    if len(a) == 1:
        if tmp < a[0]:
            cnt += 1
            res.append('L')
        break
    if a[0] < a[-1]: 
        if tmp < a[0]: # 왼쪽끝
            tmp = a[0]
            cnt += 1
            res.append('L')
            a.popleft()
            
        elif tmp < a[-1]: # 오른쪽끝
            tmp = a[-1]
            cnt += 1
            res.append('R')
            a.pop()
        
        else:
            break


    elif a[0] > a[-1]:
        if tmp < a[-1]: # 오른쪽끝
            tmp = a[-1]
            cnt += 1
            res.append('R')
            a.pop()
            
        elif tmp < a[0]: # 왼쪽끝
            tmp = a[0]
            cnt += 1
            res.append('L')
            a.popleft()
            
        else:
            break

print(cnt)
for x in res:
    print(x,end=' ')

