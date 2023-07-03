# 바둑이 승차 (DFS)

import sys
# sys.stdin = open("input.txt","rt")

# 답안 - 내 답안과 거의 같은데 시간 개선을 위한 추가 코드 있음
def DFS(L,sum,tsum):
    global result
    # 시간 개선 위해 추가한 코드
    # 바둑이들의 총 무게 total에서 tsum(이미 넣을지 안넣을지 판단이 끝난 무게)를 뺀 값 = 판단이 남은 나머지 무게
    # 그 무게에 이미 담기로 한 무게들을 더한 sum을 합친 값이 기존 최댓값인 result 보다 작다면 더이상 진행할 의미가 없으니 return 
    # (남은 바둑이들을 모두 더했는데도 최댓값을 넘지 못한다는 뜻이니 더 진행 X)
    if sum+(total-tsum)<result:
        return
    if sum>c:
        return
    if L==n: # 부분집합 하나 완성
        if result<sum:
            result=sum
    else:
        DFS(L+1,sum+a[L],tsum+a[L])
        DFS(L+1,sum,tsum+a[L])

if __name__=="__main__":
    c,n = map(int,input().split())
    a=[0]*n
    result = -2147000000
    for i in range(n):
        a[i]=int(input())
    total = sum(a)
    DFS(0,0,0)
    print(result)

'''# 내 답안 - 풀긴 했는데 3번부터 Time error 발생
def DFS(L,sum):
    global maxx
    if sum>c:
        return
    if L==n:
        if maxx<sum:
            maxx=sum
    else:
        DFS(L+1,sum+arr[L])
        DFS(L+1,sum)

if __name__=="__main__":
    c,n = map(int,input().split())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    maxx = 0
    DFS(0,0)
    print(maxx)'''