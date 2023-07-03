# 재귀함수를 이용한 이진수 출력

import sys
sys.stdin = open("input.txt","rt")

# 답안 - 훨씬 간단
def DFS(x):
    if x==0:
        return
    else:
        DFS(x//2)
        print(x%2,end=" ")

'''# 내 답안 - 맞춤 ! (근데 수정함 - 답안 참고)
# 이진수 구하는 과정 제대로 알고 수정함
def DFS(x):
    if x != 0:
        DFS(x//2)
        print(x%2,end=" ")'''

# 이거 자꾸 왜 해주는겨
if __name__=="__main__":
    n = int(input())
    DFS(n)