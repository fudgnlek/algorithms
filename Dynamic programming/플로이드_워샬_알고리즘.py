'''
< 플로이드 워샬 알고리즘 >
그래프에서 모든 정점에서 모든 정점으로 가는 최소거리를 구하는 알고리즘
dis table은 2차원이어야함, 냅색 알고리즘과 동일한 개념
dis table 초기화는 인접행렬로 설정 (직행하는데 드는 비용)
직행한 값과 어떤 노드들을 거쳐서 가는 경우 중 최소값을 table에 저장
거치는 노드의 순서는 순열이다 (꼭 순서대로가 아니어도 됨 52314 뭐 이래도 가능 - 최소거리)
'''

import sys
sys.stdin=open("input.txt","r")
input=sys.stdin.readline

n,m=map(int,input().split())
# 답안은 5000으로 설정
dis=[[2147000]*(n) for _ in range(n)]

# 인접행렬 초기화
for i in range(m):
    a,b,v=map(int,input().split())
    dis[a-1][b-1]=v
for i in range(n):
    dis[i][i]=0

# 노드 거치는 경우와 그냥 가는 경우 중 최솟값을 행렬에 저장
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i!=j:
                dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])

'''# 못가는 경우를 M으로 바꿔줌
for i in range(n):
    for j in range(n):
        if dis[i][j]==2147000:
            dis[i][j]='M'

# 행렬 출력 (한 줄씩)
for i in range(n):
    for j in range(n):
        print(dis[i][j],end=' ')
    print()'''

# 답안에서 출력을 합쳐서 코드 작성함
for i in range(n):
    for j in range(n):
        if dis[i][j]==2147000:
            print("M",end=' ')
        else:
            print(dis[i][j],end=' ')
    print()
