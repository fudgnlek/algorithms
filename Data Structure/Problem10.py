# 최소힙

# 부모는 자신의 자식보다 작아야 함

# 최소힙 구성 과정 (push) -> up hip (밑에서부터 부모와 비교하며 올라감)
# level순으로 (왼쪽부터) 채워나감 
# 들어오면 부모와 크기차이 비교해서 자식이 더 작다면 부모와 swap (한번만 하는게 아니라 자신의 부모보다 클때까지 검사)
# 들어왔을 때 부모보다 자식이 크다면 그냥 멈춤

# 최소힙에서 pop 했을 경우 -> down hip (위에서부터 자식과 비교하며 내려감)
# root 노드 값이 pop되는 순간에 가장 밑 level의 오른쪽 node값을 root로 넣어줌
# 그 상태에서 다시 최소힙 만드는 과정을 수행
# 자식들 중에 더 작은 값과 비교하여 자식이 더 작다면 swap (자신의 자식 중 작은 값보다 자신이 작은 경우까지 검사)

# 형태를 직접 그려보면서 시뮬돌려보기 ! (면접에서 그런거 하나하나 물어볼수도있음)

import sys
import heapq as hq
# sys.stdin = open("input.txt","rt")

a = []
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            # heappop() 함수가 a에서 값 하나 빼옴 (heap구조라면 그것이 root node 값)
            print(hq.heappop(a))
    else:
        # a라는 list에 n값을 push (heappush()-> 최소힙 구조로 push)
        hq.heappush(a,n)