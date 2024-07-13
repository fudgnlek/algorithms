# 후위 표기식 만들기

import sys
# sys.stdin = open("input.txt","rt")

# 숫자를 만나면 바로 출력
# 연산자를 만난 경우 stack을 확인해서 자기보다 우선순위인 연산자가 있으면 그걸 pop시키고 자기가 append
# +,-의 경우 stack에 있는 연산자 모두 출력해야함 (+,-보다 우선순위가 낮은 연산자가 없는데 이미 stack에 있다는 뜻은 중위표기식에서 더 왼쪽이라는 뜻이니까)
# 여는 괄호의 경우 무조건 stack에 넣어줌 (닫는 괄호를 만났을 때 pop 가능)
# 닫는 괄호의 경우 괄호 안의 연산자가 최우선이니까 해당 연산자들 모두 처리해야함 (괄호 모두 pop)
# 탐색이 끝난 경우 stack에 남아있다면 빌때까지 pop

a = input()
stack = []
res=''

for x in a:
    # 숫자인 경우
    if x.isdecimal():
        res+=x
    # 연산자의 경우
    else:
        if x=='(':
            stack.append(x)
        elif x=='*'or x=='/':
            # stack 비어있으면 안됨
            while stack and (stack[-1]=='*'or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x=='+'or x=='-':
            # 만약 여는 괄호가 있다면 해당 연산자가 +,-여도 괄호 안의 연산자이므로 우선순위 높음
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(':
                res+=stack.pop()
            stack.pop() # 여는 괄호 끄집어내기
# 남아있는 것들 모두 pop
while stack:
    res+=stack.pop()

print(res)