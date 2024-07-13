# 회장뽑기 (플로이드-워샬 응용)
import sys
# sys.stdin=open("input.txt","r")
input=sys.stdin.readline

n=int(input())
dis=[[5000]*(n) for _ in range(n)]

# 친구사이 인접행렬로 초기화
while True:
    a,b=map(int,input().split())
    if a==-1:
        break
    dis[a-1][b-1]=dis[b-1][a-1]=1
for i in range(n):
    dis[i][i]=0

# 건너건너 친구사이 점수 매겨서 행렬 값 설정
for k in range(n):
    for i in range(n):
        for j in range(n):
            dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])

# 각 회원 점수 구하기
res=[]
for arr in dis:
    res.append(max(arr))

# 최소 점수를 가진 회원만 저장
tot=[]
for i in range(n):
    for j in range(n):
        if res[i]>res[j]:
            break
    else:
        tot.append(i+1)

# 답안 출력
print(res[tot[0]-1],len(tot))
for i in range(len(tot)):
    print(tot[i],end=' ')

''' 답안
res=[0]*(n)
score=100
for i in range(n):
    for j in range(n):
        res[i]=max(res[i],dis[i][j])
    score=min(score,res[i])
out=[] # 내 답안에서의 tot인듯
for i in range(n):
    if res[i]==score:
        out.append(i)
print("%d %d" %(score,len(out)))
for x in out:
    print(x,end=' ')
'''



