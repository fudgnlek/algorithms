# 동전 분배하기 (DFS)

import sys
# sys.stdin = open("input.txt","rt")

# 답안 - 혼자 못품 (세명에게 나눠주는 걸 3칸의 배열로 생성해서 각 배열 값을 sum으로 두고 for문 돌려줌)
# 상태트리에서 노드 처리하고 위로 올라가는 경우 (back) 배열 값에서 다시 해당 동전 값을 빼주는 부분 주의 (중복 제거할때 checklist 했던것처럼)
def DFS(L):
    global res
    if L==n:
        cha = max(a)-min(a)
        if res>cha:
            tmp=set() # 각 나눠받은 동전의 값이 다 달라야함
            for x in a:
                tmp.add(x)
            if len(tmp)==3: # 다 달라서 중복제거가 안됨 -> 길이가 3 인 경우에만 res 업데이트
                res=cha
    else:
        for i in range(3):
            a[i]+=p[L] # 해당 사람한테 동전 나눠줌 (해당 값 증가)
            DFS(L+1) # 다음 동전으로 감
            a[i]-=p[L] # 돌아감 (나눠줬던 동전을 취소)

if __name__=="__main__":
    n = int(input())
    a=[0]*3
    p=[]
    for _ in range(n):
        p.append(int(input()))
    res = 2147000000
    DFS(0)
    print(res)