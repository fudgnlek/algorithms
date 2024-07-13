# 인접행렬 (가중치 방향그래프)

# 노드와 간선의 집합을 그래프라고 함 (뱡향이 설정되어있고, 간선 값까지 설정되어 있다면 가중치 방향그래프)
# 이차원 리스트로 행렬을 표현 (0이면 갈 수 없다는 뜻) : 항상 행번호에서 열번호로 가는 걸로 생각하기
# 무방향 그래프라면 g[a][b]=1, g[b][a]=1 이렇게 체크 (한쪽에서 갈 수 있다면 다른쪽에서도 갈수있으니까)
import sys
sys.stdin = open("input.txt","rt")

# n은 노드번호, m은 간선의 개수
n,m=map(int,input().split())
# g는 그래프 (1번부터 n번까지 있어야하니까 n+1개로 생성)
g=[[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    # 간선 정보를 입력받아서 해당하는 부분은 1로 변경해줌 (갈 수 있다는 의미)
    a,b,c=map(int,input().split())
    g[a][b]=c

for i in range(1,n+1):
    for j in range(1,n+1):
        print(g[i][j],end=' ')
    print()


'''# 무방향 그래프 코드 (다른 예로 수행함)
# n은 노드번호, m은 간선의 개수
n,m=map(int,input().split())
# g는 그래프 (1번부터 n번까지 있어야하니까 n+1개로 생성)
g=[[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    # 간선 정보를 입력받아서 해당하는 부분은 1로 변경해줌 (갈 수 있다는 의미)
    a,b=map(int,input().split())
    g[a][b]=1
    g[b][a]=1

for i in range(1,n+1):
    for j in range(1,n+1):
        print(g[i][j],end=' ')
    print()'''