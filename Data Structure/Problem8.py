# 단어찾기 (해쉬)

import sys
# sys.stdin = open("input.txt","rt")

# 답안 참고 - dict 자료형 공부 더 필요
n = int(input())
p = dict()

for _ in range(n):
    temp = input()
    p[temp] = 1
for _ in range(n-1):
    temp = input()
    p[temp] = 0
for key,val in p.items(): 
    if val==1:
        print(key)
        break
