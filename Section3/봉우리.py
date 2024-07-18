import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
a = [[0]*(n+2) for _ in range(n+2)]
for i in range(1,n+1):
    a[i] = list(map(int,input().split()))
    a[i].insert(0,0)
    a[i].append(0)
'''
답안은 2차원 배열을 입력받고
a.insert(0,[0]*n)
a.append([0]*n)
이렇게 앞뒤로 배열을 추가해주고
for x in a:
    x.insert(0,0)
    x.append(0)
이렇게 각 배열에도 0을 앞뒤로 추가해줌
결과적으로 내 코드와 비교했을 때 for문을 두번 사용하는건 똑같은 듯
'''

dx = [0,1,0,-1] # 상우하좌
dy = [-1,0,1,0]

cnt = 0 # 봉우리 개수

for i in range(1,n+1):
    for j in range(1,n+1):
        tmp = a[i][j]
        for k in range(4):
            if tmp <= a[i+dx[k]][j+dy[k]]: # 봉우리 아님
                break
        else: # 봉우리임
            cnt += 1
        '''
        답안은 if all을 사용해서 
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
        이렇게 구현함
        '''

print(cnt)