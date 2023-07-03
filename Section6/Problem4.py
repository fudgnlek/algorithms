# 합이 같은 부분집합 (DFS)

import sys
# sys.stdin = open("input.txt","rt")

# 답안 - 혼자 못품
def DFS(L,sum):
    # L : arr 인덱스 번호 (tree의 level이라는 의미도 있음)
    if sum>total//2: # 시간복잡도 개선 (반 한것보다 sum이 커버리면 더 진행해도 sum 두개를 더해서 total일수가 없으니까)
        return
    if L==n:
        if sum==total-sum:
        # if sum==total//2: # 이렇게 하면 안되는 경우 존재 (홀수는 YES일수가 없는데 //이렇게 해서 나오는 경우 있음)
            print('YES')
            sys.exit(0) # 프로그램 종료 (함수 종료가 아니라 프로그램 자체를 종료)
    else:
        DFS(L+1,sum+arr[L]) # 해당 원소 넣겠다
        DFS(L+1,sum) # 해당 원소 넣지 않겠다


if __name__=="__main__":
    n = int(input())
    arr = list(map(int,input().split()))
    total=sum(arr)
    DFS(0,0)
    print('NO') # DFS 함수 안에서 프로그램 종료가 되지 않고 왔다면 NO 출력