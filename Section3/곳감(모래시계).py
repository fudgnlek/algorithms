import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

m = int(input())
for _ in range(m):
    r,d,c = map(int,input().split()) # 행, 방향, 횟수
    tmp = a[r-1] # 타겟 행
    if d == 0: # 왼쪽
        '''
        회전하는 부분에서 pop하고 append 하는 아이디어 생각 못함 (강의 참고)
        '''
        for _ in range(c):
            num = tmp.pop(0)
            tmp.append(num)
    else:
        for _ in range(c):
            num = tmp.pop(n-1) # 그냥 pop()이랑 동일, 괄호안에 인덱스 번호 들어가는 듯
            tmp.insert(0,num) # insert(넣고 싶은 위치 인덱스, 넣고 싶은 값)

s=0
e=n-1
res = 0
for i in range(n):
    for j in range(s,e+1):
        res += a[i][j]
    if i>=n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1

print(res)