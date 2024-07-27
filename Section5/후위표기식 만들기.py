import sys
# sys.stdin = open("input.txt","rt")
'''
아예 모르겠어서 강의 보면서 코드 작성함
'''
a = input()
stack = []
res = ''

for x in a:
    if x.isdecimal(): # 숫자인 경우 (피연산자인 경우)
        res+=x
    else: # 연산자인 경우
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':
            # stack 최상단이 곱하기이거나 나누기인 경우(나보다 우선순위 높음 - 먼저 나와있었으니까)
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res += stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            # 괄호 안의 더하기 or 빼기
            while stack and stack[-1]!='(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1]!='(':
                res += stack.pop()
            stack.pop() # 여는 괄호 제거 (닫는 괄호 만났으니까)
# for문 다 돌았는데도 stack에 연산자 남아있다면 순서대로 끄집어내기
while stack:
    res += stack.pop()
print(res)

