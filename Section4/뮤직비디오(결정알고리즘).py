import sys
# sys.stdin = open("input.txt","rt")

n,m = map(int,input().split())
song = list(map(int,input().split()))

def cal(mid):
    cnt = 1
    tmp = 0
    for x in song:
        if tmp+x <= mid:
            tmp += x
        else:
            cnt += 1
            tmp = x
            ''' 
            이 경우는 새로운 dvd에 곡을 넣는 경우로
            한 dvd의 용량이 해당 곡보다는 크다는 것을 가정하고 있음
            그렇기 때문에 아래에 조건을 추가해줘야함 (아니면 반례 발생)
            * 하나의 곡을 쪼개서 넣을 수 없기 때문
            '''
    return cnt


# maxx = max(song)
lt = max(song) # 최소 용량 크기 최솟값
rt = sum(song) # 최댓값
res = 0

while lt <= rt:
    mid = (lt+rt)//2
    ''' 가장 긴 노래보다는 dvd 하나의 용량이 크거나 같아야 하는 조건 추가
    (답안에서는 이렇게 했지만 그냥 lt를 가장 긴 노래 길이로 하면 될듯)'''
    if cal(mid) <= m:
        res = mid
        rt = mid-1
    else: # elif cal(mid) > m: 했다가 안돌아감
        lt = mid+1

print(res)

