import sys
# sys.stdin = open("input.txt","rt")

a = input()
stack = []

for x in a:
    if x.isdecimal(): # 피연산자일 경우
        stack.append(int(x))
    else: # 연산자인 경우
        x2 = stack.pop()
        x1 = stack.pop()
        if x == '+':
            stack.append(x1+x2)
        elif x == '-':
            stack.append(x1-x2)
        elif x == '*':
            stack.append(x1*x2)
        else:
            stack.append(x1/x2)
print(stack.pop()) # 답안은 print(stack[0]) 이라고 함