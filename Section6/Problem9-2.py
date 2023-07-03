# 라이브러리를 이용한 순열 (수열 추측하기)

# 라이브러리에 너무 의존하면 안됨 
# -> 코테 시험에 따라 라이브러리 사용을 제한하는 경우나 특정 조건을 만족하는 수만 뽑아라 등의 경우에는 라이브러리 사용 불가
import sys
import itertools as it # 순열이나 조합을 자동으로 구해주는 라이브러리
sys.stdin = open("input.txt","rt")
n,f = map(int,input().split())

# 이항계수 초기화 후 구하기
b=[1]*n
for i in range(1,n):
    b[i]=(b[i-1]*(n-i))//i
a=list(range(1,n+1))
cnt=0

# a에서 순열이 완성되어지면 tmp에 저장됨 (a)
# a에서 3가지의 수만 뽑은 경우의 순열이 완성되어지면 tmp에 저장됨 (a,3)
for tmp in it.permutations(a):
    sum=0
    # 이때 L은 인덱스 번호 (이항계수를 인덱스에 따라 곱해야하니까 필요)
    for L,x in enumerate(tmp):
        sum+=(x*b[L])
        '''print(L,x)
    break # 첫번째 순열만 출력하려고 break'''
    if sum==f:
        for x in tmp:
            print(x,end=' ')
        break # 출력은 하나만 하면 되니까 찾고 출력하면 for문 break함