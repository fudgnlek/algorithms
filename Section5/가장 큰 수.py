import sys
sys.stdin = open("input.txt","rt")

'''
스택 - LIFO
들어가는 입구와 나오는 출구가 한 곳
(>> 나중에 들어간게 먼저 나올 수 밖에 없음)
list를 사용해서 pop과 append를 사용하면 뒷자리에서 빠지고 뒷자리에 추가되므로
stack 구현 가능
'''

n,m = map(int,input().split())
# n = str(n)
# a = list(n)

# 답안 참고 - 이런식으로 문자열 형태로 만든 n을 map이 하나하나 int화 시킴
n = list(map(int,str(n)))
stack = []
for x in n:
    # stack이 비어있지 않고, 제거 횟수가 남았고, 내가 stack의 맨 마지막 수보다 클 경우
    while stack and m>0 and stack[-1]<x:
        # stack의 맨 마지막 수를 제거
        stack.pop()
        m -= 1 # 하나 제거했으니까 -1
    stack.append(x) # 나보다 작은, 지울 수 있는 수 모두 제거 후 나를 추가
if m != 0:
    stack = stack[:-m] # 제거 횟수가 남은 경우 뒤에서 그만큼을 잘라줌
for x in stack:
    print(x,end='')
''' 답안의 출력 방법
# stack에 있는 정수를 string으로 바꿔서 join 시켜줌
res = ''.join(map(str,stack))
print(res)
'''