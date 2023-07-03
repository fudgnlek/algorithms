# 최대점수 구하기 (DFS)

import sys
# sys.stdin = open("input.txt","rt")

# 내 답안 + 답안 참고
def DFS(L,s,t):
    global maxx
    if t>m:
        return
    if L==n:
        if maxx<s:
            maxx=s
        return
    else:
        DFS(L+1,s+arr[L][0],t+arr[L][1])
        DFS(L+1,s,t)

if __name__=="__main__":
    n,m=map(int,input().split())
    arr=[]
    for _ in range(n):
        s,t = map(int,input().split())
        arr.append((s,t))
    arr.sort(reverse=True)
    maxx = -2147000
    DFS(0,0,0)
    print(maxx)