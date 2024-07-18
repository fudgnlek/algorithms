import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
apple = [list(map(int,input().split())) for _ in range(n)]
res = 0
s=e=n//2

for i in range(n):
    for j in range(s,e+1):
        res += apple[i][j]
    if i+1<=(n//2): # i < n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)

'''
답안 참고해서 품
s와 e를 중간값으로 잡고 인덱스 조정하는 아이디어 생각못함
'''