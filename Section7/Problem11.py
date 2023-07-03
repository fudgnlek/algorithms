# 등산경로 (DFS)

import sys
# sys.stdin = open("input.txt",'rt')

# 내 답안 - 맞춤 !
# 답안과 다른점 - 최소,최대값 찾을때 한 행씩 탐색해서 찾아주고 배열에 입력해줌
# - 체크 배열 사용 (근데 어차피 더 큰 구역을 찾아서 가는건데 중복이 일어날수가 없지않나 ? 안사용해도 맞긴한데 왜 굳이 사용한건지 의문)
def DFS(x,y,h):
    global cnt
    if p[x][y]==M:
        cnt+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<=n-1 and 0<=yy<=n-1 and h<p[xx][yy]:
                DFS(xx,yy,p[xx][yy])

if __name__=="__main__":
    n=int(input())
    p=[list(map(int,input().split())) for _ in range(n)]
    cnt=0
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    m=2147000
    M=0
    x=0
    j=0
    for i in range(n):
        for j in range(n):
            if p[i][j]<m:
                m=p[i][j]
                x=i
                y=j
            if p[i][j]>M:
                M=p[i][j]
    DFS(x,y,0)
    print(cnt)
