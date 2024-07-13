# 회의실 배정 (그리디)

import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
# time = [list(map(int,input().split())) for _ in range(n)]

# cnt = 1
# res = 0

# 답안 - 다 맞는데 5번은 time error 뜸
meeting = []
for i in range(n):
    s,e = map(int,input().split())
    meeting.append((s,e)) # tuple 형태로 받음
# 기준을 설정해주는데 x가 meeting 이라는 tuple의 자료
# x[1] (끝나는 시간)을 기준으로 먼저 정렬하고 그게 같다면 x[0] (시작 시간)을 기준으로 정렬해라 
meeting.sort(key=lambda x : (x[1],x[0]))
# meeting.sort() # 이렇게 하면 앞의 것 (x[0] 기준으로 먼저 정렬함)

et = 0 # 회의 끝나는 시간
cnt = 0
for s,e in meeting:
    if s>=et:
        cnt+=1
        et=e

print(cnt)



'''# 내 답안 - 맞는것도 있는데 틀린것도 있고 3번부터는 time error 뜸
# 문제 - 어떤 회의가 먼저 시작하냐에 따라 cnt를 각각 구해서 더 큰 값을 구하는 형식으로 코드를 짰는데
# 그게 아니라 먼저 끝나는 시간을 기준으로 정렬해서 그냥 cnt를 구하면 되는 문제였음...
for i in range(n):
    temp = time[i][1]
    # 크거나 같은 경우 회의 가능 ! (답안 참고)
    for j in range(i+1,n):
        if(time[j][0]>=temp):
            cnt+=1
            temp = time[j][1]
    if(res<cnt):
        res = cnt
        cnt = 1

print(res)'''
