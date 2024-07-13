# 주사위 게임

import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
result = 0

'''# 답안 
for i in range(n):
    temp = input().split() # 문자열 리스트로 받아짐
    temp.sort()
    a,b,c = map(int,temp) # int형으로 정렬되어 들어감
    if a==b and b==c: # if 문이 참이면 밑의 elif문은 실행하지 않으므로 조건이 제일 까다로운 모두 같은 경우부터 해줘야 함
        money = 10000+a*1000
    elif a==b or a==c: # 두개의 눈만 같은 경우를 나누는 이유는 상금 계산할 때 같은 눈을 정하기 쉽게 하기 위해 ! (이 경우 a)
        money = 1000+a*100
    elif b==c:
        money = 1000+b*100
    else:
        money = c*100 # 정렬되어있기 때문에 가장 큰 수는 c
    if money>result:
        result = money
print(result) '''

# 내 답안 - elif문 답안 참고함
num = [list(map(int,input().split())) for row in range(n)] # 2차원 리스트 형태로 입력받음 (블로그 참고)

for i in range(len(num)):
    if(num[i][0]==num[i][1]==num[i][2]):
        money = 10000+num[i][0]*1000
    elif(num[i][0]!=num[i][1]!=num[i][2]):
        money = max(num[i])*100
    elif(num[i][0]==num[i][1] or num[i][0]==num[i][2]):
        money = 1000+num[i][0]*100
    elif(num[i][1]==num[i][2]):
        money = 1000+num[i][1]*100
    if(result<money):
        result = money

print(result)

