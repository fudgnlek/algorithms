# 가장 큰 수
# 스택 - LIFO (나중에 들어간게 먼저 나옴), 나오고 들어가는 입구가 하나임
# 리스트를 이용하면 pop을 하면 제일 뒷 자료가 나옴 -> 리스트를 가지고 append하고 pop하면 스택 바로 구현 가능 !

import sys
# sys.stdin = open("input.txt","rt")

# 답안 (혼자 못품)
# 숫자 하나하나 검사 (자기 앞에 있는 숫자가 자기보다 커야함 작으면 삭제하고 자기가 앞으로 감)
n, m = map(int,input().split())

n=list(map(int,str(n))) # 하나하나 string으로 바꿔서 하나하나 접근가능하도록 함
stack = []
for x in n:
    # stack이 비어있지 않고, 제거 갯수가 0 이상이고 마지막 수가 자신보다 작을 경우
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    # 제거 갯수가 남았을 경우 뒤쪽 m개의 자료를 제거해줌
    stack=stack[:-m]

# stack 리스트에 있는게 하나하나가 정수라서 그걸 str으로 바꿔주고 join 시켜줌
res=''.join(map(str,stack))
print(res)

# 이렇게 출력해도 됨
# for x in stack:
#     print(x,end='')