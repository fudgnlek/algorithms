# 이진트리 순회 (깊이우선탐색 - 밑이 있으면 마지막 밑까지 계속 파고들어가는 것 막히면 back해서 다시 파고들어감)

import sys
sys.stdin = open("input.txt","rt")

# 전위순회 : 함수 자신의 본연의 일을 처리하고 밑으로 들어감 (부 - 왼 - 오) --> 대표적으로 쓰임
# 중위순회 : 출력 순서가 왼 - 부 - 오
# 후위순회 : 출력 순서가 왼 - 오 - 부모 --> 병합정렬이 대표적
# 부모*2 = 왼, 부모*2+1 = 오

def DFS(v):
    if v>7:
        return
    else:
        ''' # 호출하기 전에 자신 본연의 일(노드값 출력)을 함 - 전위순회
        print(v,end=' ')'''
        DFS(v*2) # 왼쪽 자식 호출
        ''' # 왼쪽 자식 호출하고 자신 본연의 일(노드값 출력)을 함 - 중위순회
        print(v,end=' ')'''
        DFS(v*2+1) # 오른쪽 자식 호출
        ''' # 왼,오 자식 모두 호출하고 자신 본연의 일(노드값 출력)을 함 - 후위순회
        print(v,end=' ')'''

if __name__ == "__main__":
    DFS(1)