# 회문 문자열 검사

import sys
# sys.stdin = open("input.txt","rt")

n = int(input())

# 내 답안 - 맞춤 !
for i in range(n):
    temp = input() # 문자열 하나가 temp에 들어옴
    temp = temp.lower() # 대소문자 구별 안하니까 모두 소문자로 바꿈 (답안에서는 대문자로 바꿈)
    length = len(temp)
    for j in range(length):
        if temp[j]!=temp[length-j-1]:
            print("#{0} NO".format(i+1))
            break
    else: 
        print("#{0} YES".format(i+1))

# 답안 - 비교 횟수와 if문 차이
for i in range(n):
    s = input()
    s = s.upper()
    # 파이썬스럽게 더 짧게 구현 (but, 직접 구현하는게 더 좋음)
    '''if s==s[::-1]: # s[::-1] 이거 자체가 문자열을 거꾸로 한 것 !
        print("#{0} YES".format(i+1))
    else:
        print("#{0} NO".format(i+1)) '''
    size = len(s)
    for j in range(size//2):  # size//2 번만 비교함 (길이가 5라면 2번만 비교해도 됨)
        if s[j]!=s[-1-j]: # 음수 인덱스는 거꾸로 간다는 사실을 사용
            print("#{0} NO".format(i+1))
            break
    else: 
        print("#{0} YES".format(i+1))
