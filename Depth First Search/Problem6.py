# 중복순열 구하기

import sys
# sys.stdin = open("input.txt","rt")
input=sys.stdin.readline # 대량의 입력을 할 때 굉장히 빨라짐
# s=input().rstrip() # 위의 문장을 사용할때 문자열 입력받을 시에는 이렇게 입력받아야함 (줄바꿈 기호 날림)

# 답안 - 혼자 못품 (이해는 했는데 혼자 다시 해봐야할듯 - 그림 그리면서)
def DFS(L):
    global cnt
    if L==m: # 하나의 중복순열 완성
        for x in res:
            print(x,end=' ')
        cnt+=1
        print()
    else:
        # 1부터 n 까지
        for i in range(1,n+1):
            res[L]=i
            DFS(L+1)

if __name__=="__main__":
    n,m = map(int,input().split())
    res=[0]*m
    cnt=0 # 총 중복순열 개수
    DFS(0)
    print(cnt)

'''# 내 답안 - 엉망임 (해결 X)
    def DFS(x):
    global cnt
    if x==n+1:
        return
    if cnt==m:
        for i in range(1,n+1):
            if ch[i]==1:
                print(i,end='*')
        print()
    else:
        if cnt==0:
            print(x+1, x+1)
            # cnt+=1
        ch[x+1]=1
        cnt+=1
        DFS(x+1)
        ch[x+1]=0
        DFS(x+1)


if __name__=="__main__":
    n,m = map(int,input().split())
    for i in range(n):
        ch=[0]*(n+2)
        cnt=0
        DFS(i)'''