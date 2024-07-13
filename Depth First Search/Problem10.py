# 조합 구하기

import sys
# sys.stdin = open("input.txt","rt")

# 답안 - 조합은 많은 응용이 되는 부분이라 중요 (제대로 이해하고 외워두는게 좋을듯)
# 여기서 s는 어떤 숫자부터 가지를 뻗을건지 결정
def DFS(L,s):
    global cnt
    if L==m:
        for x in res:
            print(x,end=' ')
        print()
        cnt+=1
    else:
        for i in range(s,n+1):
            res[L]=i
            # s+1이 아니라 i+1임 (주의)
            DFS(L+1,i+1)

if __name__=="__main__":
    n,m=map(int,input().split())
    res=[0]*m
    cnt=0
    DFS(0,1)
    print(cnt)

'''# 내 답안 - 틀린거 존재 (끼워맞춘 느낌이라 못맞췄다고 봐야할듯)
def DFS(L):
    global cnt
    if L==m:
        for x in res:
            print(x,end=' ')
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                res[L]=i
                ch[i]=1
                DFS(L+1)
                if L==m-1:
                    ch[i]=0
                if L==0:
                    for j in range(i+1,n+1):
                        ch[j]=0
                    for j in range(1,i+1):
                        ch[j]=1

if __name__=="__main__":
    n,m=map(int,input().split())
    res=[0]*m
    ch=[0]*(n+1)
    cnt=0
    DFS(0)
    print(cnt)'''