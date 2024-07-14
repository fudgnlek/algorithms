import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
arr1 = list(map(int,input().split()))
m = int(input())
arr2 = list(map(int,input().split()))

res = arr1+arr2
res.sort()

for x in res:
    print(x, end=' ')

'''
답안 - 이미 정렬되어 입력되는 경우이므로 sort() 내장함수를 사용하기 보다는 다음과 같이 하는게 시간복잡도가 더 좋다
p1 = p2 = 0
c = []
while p1<n and p2<m:
    if a[p1]<=b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
if p1 < n:
    c = c+a[p1:]
if p2 < m:
    c = c+b[p2:]
'''