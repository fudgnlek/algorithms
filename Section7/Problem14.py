# 안전영역 (BFS or DFS)
# 격자판을 탐색하면서 특정 영역의 넓이를 찾아내는 등의 문제는 DFS,BFS 둘 다 상관없음

import sys
# sys.stdin = open("input.txt","rt")
sys.setrecursionlimit(10**6) # 파이썬에서 재귀 사용할때 필요 (해당 시간이 넘어가면 자동으로 재귀 종료시킴)
# 이걸 해줘야 백준 사이트 같은 곳에서도 채점 됨 (입력 빡실때 필요)
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 답안 - 혼자 못품... (제대로 이해 다시 해보기)
def DFS(h,x,y):
    ch[x][y]=1
    for k in range(4):
        xx=x+dx[k]
        yy=y+dy[k]
        # 좌표 범위 설정, 높이보다 높아야하는 조건, 중복 예방
        if 0<=xx<=n-1 and 0<=yy<=n-1 and w[xx][yy]>h and ch[xx][yy]==0:
            DFS(h,xx,yy)

if __name__=="__main__":
    n=int(input())
    w = [list(map(int,input().split())) for _ in range(n)]
    # 이차원 리스트의 최댓값 구하는 다른 방법 답안에서 알려줌 (이중 for문 사용 X)
    '''tmp=-1 # 최대값
    for i in range(n):
        for j in range(n):
            if tmp<w[i][j]:
                tmp=w[i][j]'''
    res=0 # 답으로 출력할 값
    cnt=0
    for h in range(100):
        cnt = 0
        # 높이가 바뀔 때마다 ch list를 새로 초기화시켜줌
        ch=[[0]*n for _ in range(n)]
        for j in range(n):
            for k in range(n):
                if w[j][k]>h and ch[j][k]==0: 
                    cnt+=1
                    DFS(h,j,k)
        # res보다 cnt가 크다면 res를 바꿔줌
        res=max(res,cnt)
        # cnt가 0이라는 말은 h가 배열 내의 최댓값이라는 뜻 - 더이상 for문 돌 필요 없음
        if cnt==0:
            break

    print(res)