# 수들의 조합

import sys
# sys.stdin = open("input.txt","rt")

# 답안 - res 배열을 만들어서 순열을 저장하지 않고 그냥 바로바로 원소들의 합을 sum에 누적하여 해결 (내 답안과 다른점)
def DFS(L,s,sum):
    global cnt
    if L==k:
        if sum%m==0:
            cnt+=1
    else:
        # 여기서 i는 배열 인덱스이기때문에 n이 아니라 n-1까지 !
        for i in range(s,n):
            res[L]=a[i]
            DFS(L+1,i+1,sum+a[i])

if __name__=="__main__":
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    m = int(input())
    cnt=0
    DFS(0,0,0)
    print(cnt)

# 내 답안 - 맞춤
def DFS(L,s):
    global cnt
    if L==k:
        if sum(res)%m==0:
            cnt+=1
    else:
        for i in range(s,n):
            res[L]=a[i]
            DFS(L+1,i+1)

if __name__=="__main__":
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    m = int(input())
    res=[0]*(k)
    cnt=0
    DFS(0,0)
    print(cnt)