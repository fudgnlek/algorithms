# 미로탐색 (DFS)

import sys
# sys.stdin = open("input.txt","rt")
# 미로탐색 (DFS)

# 내 답안에 답안 참고해서 수정 (답안과 else문 살짝 순서 다름)
# DFS함수 내 if문 사용관련해서 제대로 이해 필요할듯 (DFS 함수 발생 순서 등)
def DFS(x,y):
    global cnt
    # 이거 안써도 되는거 이해함 (기억하기) - 원래 내 답안에는 있었음
    # if x>6 or y>6:
    #     return
    if x==6 and y==6:
        cnt+=1
    else:
        # 상하좌우
        for i in range(4):
            if 0<=x<=6 and 0<=y<=6 and p[x][y]==0:
                p[x][y]=1
                DFS(x+dx[i],y+dy[i])
                p[x][y]=0


if __name__=="__main__":
    p=[list(map(int,input().split())) for _ in range(7)]
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    cnt=0
    # p[0][0]=1 # 체크해줌
    DFS(0,0)
    print(cnt)

'''# 내 답안 - 답안 참고해서 맞춤
def DFS(x,y):
    global cnt
    if x>6 or y>6:
        return
    if x==6 and y==6:
        cnt+=1
    else:
        # 상하좌우
        for i in range(4):
            if 0<=x<=6 and 0<=y<=6 and ch[x][y]==0 and p[x][y]==0:
                ch[x][y]=1
                DFS(x+dx[i],y+dy[i])
                ch[x][y]=0


if __name__=="__main__":
    p=[list(map(int,input().split())) for _ in range(7)]
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    cnt=0
    ch=[[0]*7 for _ in range(7)]
    DFS(0,0)
    print(cnt)'''


