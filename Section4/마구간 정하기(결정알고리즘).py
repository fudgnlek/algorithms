import sys
# sys.stdin = open('input.txt',"rt")

n,c = map(int,input().split())
a = []
for _ in range(n):
    a.append(int(input()))
a.sort()

def cal(mid):
    cnt = 1
    tmp = a[0]
    for i in range(1,n):
        if a[i] >= tmp+mid:
            cnt += 1
            tmp = a[i]
    return cnt # 놓을 수 있는 말의 갯수

# 강의에서 힌트얻음 (최대 거리를 이분탐색으로 두고 둘 수 있는 말 개수 비교)
lt = 1
rt = a[-1]
res = 0

while lt <= rt:
    mid = (lt+rt)//2
    if cal(mid) >= c:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)
