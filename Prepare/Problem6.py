# 자릿수의 합

import sys
sys.stdin = open("input.txt","rt")

n = int(input()) # 몇 개의 자연수 입력할지
num = list(map(int,input().split())) # 입력된 자연수들
max = -2147000000 

# 답안 - 자릿수 합 더하는 두가지 방법 모두 알고있기 !

'''def digit_sum(x):
    sum = 0 
    while (x>0):
        sum += x%10
        x = x//10 # 수를 10으로 나눈 몫
    return sum '''

# 더 편한 방법 : 숫자를 문자화 시켜주면 됨
def digit_sum(x):
    sum = 0
    for i in str(x): # 이렇게 하면 문자열로 인식해서 문자 하나하나가 i에 들어감 !
        sum += int(i)
    return sum

for x in num: # 이렇게만 해도 리스트안에 있는 수 하나씩 접근함
    total = digit_sum(x)
    if(total>max):
        max = total
        res = x

print(res)

# 알게 된 것 : 나눈 몫을 정수로 표현하고 싶을 때는 // 사용 !
# 자릿수 구하는 방법 답안 외우기 !

# # 내 답안 (잘되는줄 알았는데 십의자리가 0인 경우 제대로 동작 X - 못푼거지...)
'''def digit_sum(x):
    sum =0 
    a = 10
    while(x//a != 0):
        s = int(x%a)
        if(s<10):
            sum += s
        else:
            s = s//(a//10)
            sum += s
        a *= 10
    a //= 10
    sum += x//a
    return sum

for i in range(len(num)):
    result = digit_sum(num[i])
    if(max < result):
        max = result
# print(max)

for i in range(len(num)): 
    if(max == digit_sum(num[i])):
        print(num[i])
        break'''


