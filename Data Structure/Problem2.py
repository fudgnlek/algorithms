# 쇠막대기

import sys
# sys.stdin = open("input.txt","rt")

'''# 답안 - 이게 훨씬 깔끔
s = input()
stack = []
cnt = 0

for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else:
        stack.pop() # 어차피 if,else문 다 하니까
        # 닫는 괄호 - 앞의 괄호를 확인
        if s[i-1]=='(': # 레이저인 경우
            # stack.pop()
            cnt+=len(stack) # 스택에 쌓여있는 것들은 잘려진 쇠막대기의 갯수니까
        else:
            # 쇠막대기의 끝인 경우
            # stack.pop() # 쇠막대기 끝났으니까 해당부분 pop 시켜줌
            cnt+=1

print(cnt)'''

# 내 답안 - 맞춤 !
string = str(input())
arr = list(map(str,string))
laz = []
pipe = []
stack = []

def Check(s,e):
    cnt = 0
    for x in laz:
        if s<x<e:
            cnt+=1
    return cnt+1

for i in range(len(arr)):
    if(arr[i]=='('and arr[i+1]==')'and i<len(arr)):
        laz.append(i) # 레이저 위치 저장
    if(arr[i]=='('):
        stack.append(i)
    if(arr[i]==')'):
        temp = stack.pop()
        if temp in laz:
            continue
        else:
            pipe.append((temp,i)) # 막대기 시작,끝 위치 저장

pipe.sort()
cnt = 0

for s,e in pipe:
    cnt+=Check(s,e)

print(cnt)