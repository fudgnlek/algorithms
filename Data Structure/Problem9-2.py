# 아나그램 (리스트 해쉬)

import sys
sys.stdin = open("input.txt","rt")

a = input()
b = input()
# 소문자, 대문자 합쳐서 총 알파벳 52개
str1=[0]*52
str2=[0]*52

for x in a:
    # 해당 문자가 대문자인지 확인
    if x.isupper():
        # ord : 해당 문자를 아스키 코드로 변환
        # 대문자 (65~90), 소문자 (97~122)
        # 대문자 인덱싱을 0~25까지 하려면 -65, 소문자 인덱싱을 26~51까지 하려면 -71 해주면 됨
        str1[ord(x)-65]+=1 # 누적 (카운팅)
    else:
        str1[ord(x)-71]+=1

for x in b:
    # 해당 문자가 대문자인지 확인
    if x.isupper():
        str2[ord(x)-65]+=1 # 누적 (카운팅)
    else:
        str2[ord(x)-71]+=1

# 구성 성분 같은지 확인
''' 이렇게 해도 됨
    if str1==str2:
    print("YES")'''

for i in range(52):
    if str1[i]!=str2[i]:
        print("NO")
        break
else:
    print("YES")
