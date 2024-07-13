# 이분검색

import sys
# sys.stdin = open("input.txt","rt")

n,m = map(int,input().split())
a = list(map(int,input().split()))

# 내 답안 -  (but, 이분검색은 아닌듯)
# 오름차순 정렬
a.sort()

# m이 몇 번째에 있는지 구하기
for i in range(n):
    if(a[i]==m):
        print(i+1)
        break

# 답안 - 이분검색
lt = 0
rt = n-1

while lt<=rt:
    mid = (lt+rt)//2
    if(a[mid]==m):
        print(mid+1)
        break
    elif(a[mid]>m):
        rt=mid-1
    else:
        lt=mid+1