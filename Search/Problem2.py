# 숫자만 추출

import sys
# sys.stdin = open("input.txt","rt")

s = input()

'''# 답안
res = 0
for x in s:
    if x.isdecimal(): # isdecimal() : 0 ~ 9 사이의 숫자면 함수 리턴값이 True
        res = res * 10 + int(x) # 숫자화 시키는 방법 (섹션 2 - 8 참고)
print(res)

cnt = 0 
for i in range(1,res+1):
    if(res%i==0):
        cnt+=1
print(cnt) '''

# 내 답안 - 맞춤 !
number = ['0','1','2','3','4','5','6','7','8','9']
result = ''

# 문자열 안에 있는 숫자만 추출
for x in s:
    if(x in number):
        result += x
n = int(result)
print(n)

# 추출한 자연수의 약수 구하기
num = []
for i in range(1,n//2):
    if(n%i==0):
        num.append(i)
        num.append(n//i)
num = set(num)
print(len(num))

