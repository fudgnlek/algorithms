# 피자 배달 거리 (삼성 SW역량평가 기출문제 : DFS활용)

import sys
# sys.stdin = open("input.txt","rt")

# 답안 (내 답안에 추가 및 수정)
# 실수한 부분 : 피자집 입장에서의 배달거리 총합이 아니라 집 입장에서의 배달거리 총합의 최소를 구하는 문제 !
# 조합 이용한 부분 미숙했음 (조합 관련 코드 제대로 외워서 사용할 수 있어야할듯)
def DFS(L,s):
    global d
    if L==m:
        sum=0
        # 집을 하나 지정하고 M개의 선택된 피자집을 쭉 for문으로 돌면서 피자배달거리 최소값을 구함
        for i in range(len(house)):
            tmp=2147
            for x in res:
                loc=abs(house[i][0]-pizza[x][0])+abs(house[i][1]-pizza[x][1])
                tmp=min(tmp,loc)
            sum+=tmp # 도시의 피자배달거리
        if sum<d:
            d=sum
    else:
        for i in range(s,len(pizza)):
            res[L]=i
            DFS(L+1,i+1)


if __name__=="__main__":
    n,m=map(int,input().split())
    p=[list(map(int,input().split())) for _ in range(n)]
    pizza=[] # 피자집 위치좌표 저장
    house=[] # 집 위치좌표 저장
    res=[0]*m
    d=2147000
    for i in range(n):
        for j in range(n):
            if p[i][j]==1: # 집인 경우
                house.append((i,j))
            if p[i][j]==2: # 피자집인 경우
                pizza.append((i,j))
    DFS(0,0)
    print(d)

