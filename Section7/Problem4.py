# 동전 바꿔주기 (DFS)

import sys
# sys.stdin = open("input.txt","rt")

# 답안 - 혼자 못품
def DFS(L,sum):
    global cnt
    if sum>t:
        return
    if L==k:
        if sum==t:
            cnt+=1
    else:
        for i in range(a[L][1]+1): # 동전이 3개면 0~3까지 돌아야함 (포함 안되는 경우부터 모두 포함하는 경우까지)
            DFS(L+1,sum+a[L][0]*i) # 해당 동전을 포함하는 만큼 sum에 더해줘야함 (해당 동전에 i를 곱해주면 됨 - i가 갯수니까)

if __name__=="__main__":
    t=int(input()) # 지폐 금액
    k=int(input()) # 동전 가지수
    a=[]
    for _ in range(k):
        p,n = map(int,input().split())
        a.append((p,n))
    cnt = 0
    DFS(0,0)
    print(cnt)
