# 휴가 (DFS)

import sys
# sys.stdin = open("input.txt","rt")

# 내 답안 - 맞춤 !
def DFS(d,p):
    global maxx
    if d>n:
        return
    if d==n:
        if maxx<p:
            maxx=p
        return
    else:
        DFS(d+a[d][0],p+a[d][1])
        DFS(d+1,p)

if __name__=="__main__":
    n = int(input())
    a = [list(map(int,input().split())) for _ in range(n)]
    maxx = -2147000
    DFS(0,0)
    print(maxx)