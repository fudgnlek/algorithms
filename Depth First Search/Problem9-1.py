# 수열 추측하기
# Feedback
# 이항계수 따로 구해서 바로 합 구해버리는 부분 생각못함

import sys
sys.stdin = open("input.txt","rt")

# 답안
# 파스칼의 원리를 알아내서 이용 -> 각 순열을 구해서 이항계수와 각각 곱하고 자리를 더하면 파스칼 마지막 숫자 구해짐
def DFS(L,sum):
    if L==n and sum==f: # 순열이 완성되었고 파스칼 합이 f와 같은 경우 (답)
        for x in p:
            print(x,end=' ')
        sys.exit(0) # 여러가지 있을 때 하나만 출력해야 하니까 프로그램 자채를 종료해버림
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                p[L]=i
                ch[i]=1
                DFS(L+1,sum+(b[L]*p[L]))
                ch[i]=0

if __name__=="__main__":
    n,f = map(int,input().split())
    p=[0]*n
    b=[1]*n # n이 뭔지에 따라 이항계수 저장할 배열
    # 이항계수를 구함 (이항계수는 끝이 항상 1) - 조합(C) 공식 사용
    for i in range(1,n):
        b[i]=(b[i-1]*(n-i))//i # 이 코드는 직접 조합 구하는거 해보면 알 수 있음
    ch=[0]*(n+1)
    DFS(0,0)

'''# 내 답안 - 맞춤 ! (채점은 못돌림 - 5초제한 채점기는 내 노트북에서 안됨)
# 근데 파스칼 순열마다 제대로 구하는거 비효율적 -> 답안이 훨씬 효율적
def DFS(L):
    if L==n:
        temp=[]
        for x in res:
            temp.append(x)
        while(len(temp)>1):
            for i in range(len(temp)-1):
                temp[i]=temp[i]+temp[i+1]
            temp.pop()
        if temp[0] == f:
            for x in res:
                print(x,end=' ')
            print()
            sys.exit(0)
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                res[L]=i
                ch[i]=1
                DFS(L+1)
                ch[i]=0


if __name__=="__main__":
    n,f = map(int,input().split())
    res=[0]*(n)
    ch=[0]*(n+1)
    DFS(0)'''
