import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
a = []
for _ in range(n):
    h,w = map(int,input().split())
    a.append((h,w))
a.sort()
cnt = 1 # 키가 가장 큰 지원자는 무조건 합격
for i in range(n-1):
    tmp = a[i][1] # 비교 대상 몸무게
    for j in range(i+1,n):
        if tmp <= a[j][1]:
            break
    else:
        cnt += 1

''' 답안 참고 (내 답도 맞긴함)
(내림차순해서 몸무게만 비교하면 굳이 이중포문 안써도 됨)
a.sort(reverse=True) # 내림차순 정렬
largest = 0
for h,w in a:
    if largest < w:
        largest = w
        cnt+=1    
'''
print(cnt)
