# 씨름선수 (그리디)

import sys
sys.stdin = open("input.txt","rt")

# 내 답안 - 맞춤 !
n = int(input())
a=[]
for i in range(n):
    h,w=map(int,input().split())
    a.append((h,w))

'''#답안 - 이중 for문 사용 안함
cnt=1
# 답안 설명 듣고 내가 짠 코드
largest = a[0][1] # 키가 제일 큰 사람의 몸무게를 일단 largest로 둠
for i in range(1,n):
    if(a[i][1]>largest):
        cnt+=1
        largest = a[i][1]
print(cnt)
# 답안 코드
largest = 0
cnt = 0
for h,w in a:
    if w>largest:
        largest = w
        cnt+=1
print(cnt)'''

# .sort() 항상 오름차순이 기본인거 기억하기 !
a.sort(reverse=True)
cnt = n

for i in range(n-1,0,-1):
    temp = a[i][1]
    for j in range(i):
        if(temp<=a[j][1]):
            cnt-=1
            break
print(cnt)
