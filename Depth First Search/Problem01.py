# [선수지식] 재귀함수와 스택

import sys
sys.stdin = open("input.txt","r")

def DFS(x):
    if x>0:
        # print(x) # 재귀함수 호출 위에 print하면 321 출력되고
        DFS(x-1) # 재귀함수
        print(x,end=' ') # 재귀함수 호출 밑에 print하면 123 출력됨 (스택을 사용하기 때문)
        # 재귀함수 호출 시 메모리에 매개변수,지역변수,복귀주소 이렇게 저장됨 (그 덩어리를 스택프레임이라고 함)
        # 스택 방식으로 저장되기 때문에 1 2 3 으로 출력됨

# main 부분
if __name__ == "__main__":
    n = int(input())
    DFS(n)