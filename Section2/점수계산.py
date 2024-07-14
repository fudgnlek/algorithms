import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
ans = list(map(int, input().split()))
score = 0 # 총 점수
cnt = 0 # 가산점 횟수
for i in range(n):
    if ans[i] == 1:
        cnt += 1
        score += cnt
    if ans[i] == 0:
        cnt = 0
print(score)