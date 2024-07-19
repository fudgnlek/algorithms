import sys
sys.stdin = open("input.txt","rt")

n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
# print(a)
print(a.index(m)+1)

# 답안 - 이분탐색 정석인듯
a.sort()
lt = 0
rt = n-1
while lt<=rt:
    mid = (lt+rt)//2
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt = mid-1
    else:
        lt = mid+1
