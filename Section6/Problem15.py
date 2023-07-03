# 경로탐색 (그래프 DFS)

import sys
sys.stdin = open("input.txt","rt")

# 내 답안 - 맞춤 ! (해당 경로까지 출력하는 부분 추가 - 답안)
def DFS(s):
    global cnt
    if s==n:
        cnt+=1
        for x in path:
            print(x,end=' ')
        print()
    else:
        # 답안에서는 range(1,n+1) 이렇게 해주고 main에서 ch[1]=1로 설정해줌 - 두 방법 모두 상관없나 ?
        for i in range(2,n+1):
            # if문 두개 쓰지않고 and 사용 (답안)
            if ch[i]==0:
                if g[s][i]==1:
                    ch[i]=1
                    path.append(i) # 경로 추가해줌
                    DFS(i)
                    ch[i]=0 # 돌아갈때 체크를 풀어줘야 다른 경우의 수를 확인할 수 있음
                    # 만약에 12345 하고 나서 1245도 가능할 수 있는데 이때 5,4 끝났을 때 체크 안풀어주면 245를 확인 못하고 지나침
                    path.pop() # 뺄 경우 pop도 해줘야 함

if __name__=="__main__":
    n,m=map(int,input().split())
    g=[[0]*(n+1) for _ in range(n+1)] # 인접행렬
    for i in range(m):
        a,b=map(int,input().split())
        g[a][b]=1
    # for i in range(1,n+1):
    #     for j in range(1,n+1):
    #         print(g[i][j],end=' ')
    #     print()
    cnt=0
    path = [] # 경로 출력을 위한 배열
    path.append(1)
    ch=[0]*(n+1) # 한번 방문한 노드를 다시 방문하면 안됨 (중복 불가)
    DFS(1)
    print(cnt)