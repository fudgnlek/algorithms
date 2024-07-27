import sys
# sys.stdin = open("input.txt","rt")

a = input()

# 답안 코드 - 훨씬 깔끔
stack = []
cnt = 0
for i in range(len(a)):
    if a[i]=='(':
        stack.append(a[i])
    else:
        # stack.pop() # 어차피 어떤 경우든 하니까 이렇게 빼도 됨
        if a[i-1]=='(': # 레이저인 경우
            stack.pop()
            # 여는 괄호가 몇개가 있든 그게 쇠막대기의 개수
            cnt+=len(stack)
        else: # 쇠막대기의 끝
            stack.pop() # 쇠막대기의 시작지점을 pop
            cnt+=1 # 쇠막대기의 마지막 조각을 카운팅
print(cnt)


# 내 코드 - 맞긴 한데 그렇게 똑똑한 코드는 아닌듯
a = list(a)

lazer = []
stick = []
tmp = [] # 완성된 쇠막대기
for i in range(len(a)):
    if a[i] == '(':
        if a[i+1] == ')': # 레이저인 경우
            lazer.append(i)
        else:
            stick.append(i)
    if (len(lazer)==0 or lazer[-1]+1 != i) and a[i] == ')': # 쇠막대기인 경우
        tmp.append((stick[-1],i))
        stick.pop()
tmp.sort()
res = [1]*len(tmp)
for x in lazer:
    for i in range(len(tmp)):
        if x < tmp[i][0]:
            break
        elif x > tmp[i][1]:
            continue
        else:
            res[i]+=1
# print(res)
print(sum(res))






