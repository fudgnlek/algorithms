# 부분집합 구하기 (DFS)

import sys
# sys.stdin = open("input.txt","rt")

# 답안 - 상태트리 (해당 숫자를 포함한거 안한걸로 자식 트리 설정)
def DFS(x):
    if x==n+1:
        for i in range(1,n+1):
            if ch[i]==1:
                print(i,end=' ')
        print()
    else:
        ch[x]=1
        DFS(x+1)
        ch[x]=0
        DFS(x+1)

if __name__=="__main__":
    n = int(input())
    ch=[0]*(n+1) # 사용한다 안한다를 표시하는 배열
    DFS(1)