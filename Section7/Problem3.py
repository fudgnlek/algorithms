# 양팔저울 (DFS)

import sys
# sys.stdin = open("input.txt","rt")

# 답안
# 상태트리가 세갈래로 나뉨 (하나는 왼쪽에 추 올리는 경우(+), 오른쪽에 올리는 경우(-), 적용하지 않는 경우)
# 그릇은 더 작은 곳에서 무게가 재졌다고 생각하기 (노드 값이 추를 통해 잴 수 있는 무게인 것)
# 대칭구조로 나타나기 때문에 음수값은 신경쓸필요 없음 (그릇이 오른쪽에 있는 경우, 왼쪽에 있는 경우 두가지로 나타나기 때문 - 중복)
# 상태트리 혼자 그려보고 제대로 다시 이해하기
def DFS(L,sum):
    global res
    if L==k:
        if 0<sum<=s: # 음수는 체크 X (ex) 1,5 vs 7 은 sum=-1, 7 vs 1,5 는 sum=1 이므로 대칭구조 존재함
            res.add(sum) # res에 추가하는 이유는 어떤 무게를 재는 방법이 1가지 이상일 수 있음 (1 or 1,5 vs 7 같은 경우처럼) - 중복 제거를 위함
    else:
        DFS(L+1,sum+g[L]) # 왼쪽에 추를 넣음
        DFS(L+1,sum-g[L]) # 오른쪽에 추를 넣음
        DFS(L+1,sum)

if __name__=="__main__":
    k = int(input())
    g = list(map(int,input().split()))
    s=sum(g) # 추 무게의 총합
    res=set() # 중복을 제거하면서 값을 추가함(set 자료형), 측정 가능한 물의 무게를 하나씩 추가
    DFS(0,0)
    print(s-len(res))


'''# 내 답안 - 해결 못함
def DFS(I,s,d,L):
    global cnt
    if L==k:
        return
    if d+I == s or I == s:
        print(s)
        cnt+=1
        return
    else:
        DFS(I,s+a[L],d,L+1) # 오른쪽에 추
        DFS(I,s,d+a[L],L+1) # 왼쪽 그릇에 추
        DFS(I,s,d,L+1) # 추 X

if __name__=="__main__":
    k = int(input())
    a = list(map(int,input().split()))
    cnt=0
    tot = sum(a)
    for i in range(1,tot+1):
        if i not in a:
            DFS(i,0,0,0)
    print(tot-cnt-len(a))'''