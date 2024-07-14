import sys
# sys.stdin = open("input.txt","rt")

word = input()
res = ""
'''
답안은 isdecimal() 함수 사용
res = 0
for x in word:
    if x.isdecimal():
        res = res*10+int(x)
print(res)
'''

'''
isdecimal()은 주어진 문자열이 int형으로 변환이 가능한지 알아내는 함수
isnumeric()은 숫자값 표현에 해당하는 문자열까지 인정(제곱근, 분수, 거듭제곱 특수문자도 인정)
isdigit()는 단일 글자가 '숫자'모양으로 생겼으면 무조건 True (숫자처럼 생긴 모든 글자를 숫자로 침)
'''
for x in word:
    if x in ['0','1','2','3','4','5','6','7','8','9']: # 숫자인 경우
        res+=x
res = int(res) # 만들어진 자연수
print(res)

# 약수의 개수
cnt = 1
for i in range(1,res//2+1):
    if res%i == 0:
        cnt += 1
print(cnt)
    