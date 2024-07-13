import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
a = list(map(int,input().split()))
average = round(sum(a)/n) # 평균
# print(average)
score = []

for idx,x in enumerate(a):
    score.append((idx+1,-x,abs(average-x)))

score.sort(key=lambda x :(x[2],x[1],x[0]))
# print(score)

print(average, score[0][0])

# 답안은 for문 (enumerate사용)에서 if,elif로 비교해서 답 구함