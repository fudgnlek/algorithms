# 동전교환

import sys
# sys.stdin = open("input.txt","rt")

# 답안 - 혼자 못품...
def DFS(L,sum):
    global res
    if sum>m:
        return
    if sum==m:
        if L<res:
            res=L
        return # 이거 안해줘도 시간 차이 별로 없는건가 ?
    # 더 cut 해주는 부분 (이미 res가 3인데 L이 4라면 더이상 진행할 필요가 없으니까)
    if L>res:
        return
    else:
        for i in range(n): # 동전 갯수만큼 돈다
            DFS(L+1,sum+a[i])

if __name__=="__main__":
    n=int(input())
    a = list(map(int,input().split()))
    m = int(input())
    a.sort(reverse=True) # 처음 출발이 1원짜리면 너무 깊게 들어감 (큰 수부터 하도록 내림차순 적용)
    res = 2147000000 # 큰 수로 둠
    DFS(0,0)
    print(res)
