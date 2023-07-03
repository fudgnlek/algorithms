# 최대힙

# 부모가 두 자식노드보다 값이 커야함 (root노드가 최대값)

import sys
import heapq as hq
# sys.stdin = open("input.txt","rt")

a = []

# heappop(), heappush() 함수 모두 최소힙 구조로 동작하기 때문에 최대힙 구조로 동작하게끔 하려면
# 들어가는 숫자의 부호를 바꿔서 절댓값이 큰 값이 위로 가도록 해놓고 
# pop할때 부호를 다시 바꿔서 출력해주면 됨
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a,-n)