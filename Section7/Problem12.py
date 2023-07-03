# 단지 번호 붙이기 (DFS,BFS)

import sys
# sys.stdin = open("input.txt","rt")
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 답안 (내 답안에 답안 참고해서 수정)
def DFS(x,y):
    global cnt
    cnt+=1
    p[x][y]=0 # 탐색한 구역은 0으로 바꿔줌 (중복 탐색 안되도록)
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<=(n-1) and 0<=yy<=(n-1):
            if p[xx][yy]==1:
                DFS(xx,yy)

if __name__=="__main__":
    n = int(input())
    # 입력에 띄어쓰기가 안되어있음 -> split() 이거 사용 안함
    p=[list(map(int,input())) for _ in range(n)]
    res=[]
    # 집이 나올때마다 DFS함수 호출
    for i in range(n):
        for j in range(n):
            if p[i][j]==1:
                cnt=0
                DFS(i,j)
                res.append(cnt)

res.sort() # 오름차순 출력을 위해 정렬
print(len(res))
for x in res:
    print(x)