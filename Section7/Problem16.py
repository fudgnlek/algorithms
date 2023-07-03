# 사다리 타기 (DFS)

import sys
sys.stdin = open("input.txt","rt")


# 답안
# 9행부터 시작해서 2가 등장하는 그 곳부터 역으로 검사해서 0행에 도착했을 때 해당 index열을 출력하는 방식
# 답안에서는 dx,dy안쓰고 그냥 if elif else 문으로 해결
dx = [0,0,-1]
dy = [1,-1,0]

def DFS(x,y):
    ch[x][y]=1 # checklist 다시 초기화 안해줘도 되는 거 이해하기
    if x==0:
        print(y)
        # sys.exit(0) # 이거 안써도 문제없네...
    else:
        for i in range(3):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<=9 and 0<=yy<=9 and ch[xx][yy]==0 and a[xx][yy]==1:
                DFS(xx,yy)
                break

if __name__=="__main__":
    a=[list(map(int,input().split())) for _ in range(10)] # 사다리 배열 입력받음
    ch = [[0]*10 for _ in range(10)] # checklist
    for i in range(10):
        if a[9][i]==2:
            DFS(9,i)


'''# 내 답안 - 못품 (하나하나 시작점부터 다 DFS 돌렸는데 답안에서 그건 너무 비효율적이라고 함)
# 답안으로 공부하기
# 오,왼,하 순서로 검색
dx = [0,0,1]
dy = [1,-1,0]

def DFS(x,y):
    global res
    if x==9: # 사다리 도착
        if a[x][y]==2: # 특정 도착지점에 도착
            res=0
        return
    else:
        for i in range(3):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<=9 and 0<=yy<=9 and a[xx][yy]==1:
                a[xx][yy]=0
                DFS(xx,yy)
                a[xx][yy]=1
                break

if __name__=="__main__":
    a=[list(map(int,input().split())) for _ in range(10)] # 사다리 배열 입력받음
    res=-1
    for i in range(10):
        if a[0][i]==1: # 사다리 출발점
            DFS(0,i)
            if res==0:
                res=i

print(res)'''             




