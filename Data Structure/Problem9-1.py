# 아나그램 (딕셔너리 해쉬)

import sys
# sys.stdin = open("input.txt","rt")

a = input()
b = input()

# 개선된 코드
sh = dict()
for x in a:
    sh[x]=sh.get(x,0)+1

for x in b:
    sh[x]=sh.get(x,0)-1

# a 문자열 검사할때 값을 1씩 올려놓고 b 문자열 검사할때 해당 값을 1씩 내려버리면
# 같은 문자인 경우 값이 0일 될 것이므로 dict 하나로 가능
for x in a:
    # a에 해당하는 문자 값들이 전부 0 이어야 b 문자열에도 존재한다는 의미인데
    # 하나라도 0 보다 큰 값이 존재하는 경우 b를 검사하는 과정에서 마이너스가 되지 않았다는 뜻 -> 아나그램이 아님
    if sh.get(x)>0:
        print("NO")
        break
else:
    print("YES")

# 답안
str1 = dict()
str2 = dict()

for x in a:
    # x라는 알파벳이 존재한다면 해당 키값의 value값을, 없으면 0을 return (get(x,0))
    str1[x]=str1.get(x,0)+1
for x in b:
    # x라는 알파벳이 존재한다면 해당 키값의 value값을, 없으면 0을 return (get(x,0))
    str2[x]=str2.get(x,0)+1

# 구성 성분이 같은지 확인
for i in str1.keys(): # key값들만 i에 대응됨
    if i in str2.keys(): # 같은 key는 존재하지만 갯수가 다른 경우
        if str1[i]!=str2[i]:
            print("NO")
            break
    else: # 같은 key가 존재하지 않는 경우
        print("NO")
        break
else: # 같은 key 존재하고 갯수도 같은 경우
    print("YES")


