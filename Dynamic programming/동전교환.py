# 동전교환
import sys
# sys.stdin=open("input.txt","r")
input=sys.stdin.readline

n=int(input())
# 이 경우 거슬러줘야 할 금액을 마지막에 입력받기 때문에
# 배열을 따로 생성해줘야함
a=list(map(int,input().split()))
m=int(input())
dy=[1000]*(m+1)
dy[0]=0

for i in range(n):
    for j in range(a[i],m+1):
        dy[j]=min(dy[j],dy[j-a[i]]+1)

print(dy[m])

# Feedback
# 냅색 알고리즘 똑같이 적용
# dy[j] : j원을 거슬러주는데 사용된 동전의 최소개수
# 이 경우 최솟값을 찾는거니까 초기화를 큰 값으로 !
# But, dy[0]=0으로 (0원을 거슬러줄땐 0이니까)




