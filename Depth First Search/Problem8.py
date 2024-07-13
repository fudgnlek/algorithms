# 순열 구하기

import sys
# sys.stdin = open("input.txt","rt")

# 내 답안 - 중복 제거 해결 못함 (-> 답안 통해 해결)
def DFS(L):
    global cnt
    if L==m:
        for x in res:
            print(x,end=' ')
        cnt+=1
        print()
    else:
        for i in range(1,n+1):
            if ch[i-1]==0:
                res[L]=i
                ch[i-1]=1
                # 여기 위쪽은 호출이 일어난 것
                DFS(L+1)
                # 중복 제거를 위한 코드 (답안)
                # 여기 아래족은 호출이 일어나고 되돌아온것
                # DFS호출이 끝날때마다 (돌아올때마다) 해당 숫자를 ch에서 다시 사용할수있도록 값을 바꿔줘야함
                ch[i-1]=0


if __name__=="__main__":
    n,m = map(int,input().split())
    res=[0]*m
    ch=[0]*n # 중복을 막기 위한 checklist
    cnt=0
    DFS(0)
    print(cnt)