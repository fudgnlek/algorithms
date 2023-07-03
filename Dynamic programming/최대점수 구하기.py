# 최대점수 구하기 (냅색 알고리즘)
import sys
# sys.stdin=open("input.txt","r")
input=sys.stdin.readline

n,m=map(int,input().split())
dy=[0]*(m+1)

for i in range(n):
    s,t=map(int,input().split())
    # 뒤에서부터 실행해서 중복을 방지
    for j in range(m,t-1,-1):
        dy[j]=max(dy[j-t]+s,dy[j])

print(dy[m])

# Feedback
# 한 유형당 한번만 풀어야하므로 다른 문제처럼 dy 배열을 1차원으로 하지 않고
# 2차원으로 해야함 (중복으로 푸는 경우를 방지하기 위해)
# dy[i-1][j-t] --> 메모리 커져서 별로 좋지 않음
# 1차원으로 가능 ! -> 중복이 발생하지 않도록 뒤에서부터 진행)

''' dfs 사용해서 해결
def dfs(s,t,l):
    global maxx
    if t>m:
        return
    if l==n:
        if maxx<s:
            maxx=s
    else:
        dfs(s+a[l][0],t+a[l][1],l+1)
        dfs(s,t,l+1)

if __name__=="__main__":
    n,m=map(int,input().split())
    a=[list(map(int,input().split()))for _ in range(n)]
    maxx=-2147000
    dfs(0,0,0)
    print(maxx)'''
