# 후위연산

import sys
# sys.stdin = open("input.txt","rt")

a = input()
stack = []
res = 0

# 답안
# 비슷한데 굳이 res를 두지 않고 어차피 맨 마지막에 stack에 남아있는게 답이니까 그걸 print함
# print(stack[0])

# 내 답안 - 맞춤 !
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    elif x=='+':
        temp=stack.pop()
        res=temp+stack.pop()
        stack.append(res)
    elif x=='-':
        temp=stack.pop()
        res=stack.pop()-temp
        stack.append(res)
    elif x=='*':
        temp=stack.pop()
        res=temp*(stack.pop())
        stack.append(res)
    elif x=='/':
        temp=stack.pop()
        res=stack.pop()/temp
        stack.append(res)
print(res)