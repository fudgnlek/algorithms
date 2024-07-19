import sys
# sys.stdin = open("input.txt","rt")

k,n = map(int,input().split())
line = []
for _ in range(k):
    line.append(int(input()))

def cal(mid):
    cnt = 0
    for x in line:
        cnt += x//mid
    return cnt

lt = 1 # 한 랜선의 길이 최솟값
rt = max(line) # 한 랜선의 길이 최댓값 (처음에 line 최솟값으로 하는 실수함)
res = 0

while lt <= rt:
    mid = (lt+rt)//2
    if cal(mid) >= n:
        # print(mid)
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)