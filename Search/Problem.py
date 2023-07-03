# 격자판 회문수

import sys
# sys.stdin = open("input.txt","rt")

arr = [list(map(int,input().split())) for _ in range(7)]

# 답안
cnt = 0
# 3번만 도는 이유는 0,1,2 만 하면 되니까 (n이 7인데 5개씩이니까 !)
for i in range(3):
    for j in range(7): # j가 행
        tmp = arr[j][i:i+5] # 슬라이싱 사용
        if(tmp==tmp[::-1]): # 회문 기억하기 (전에 나왔었음 거꾸로 해서 같으면 회문 !)
            cnt+=1
        # 세로 비교 (세로로는 일차원 리스트가 아니라서 슬라이싱이 안됨)
        for k in range(2): # 5개짜리 회문 비교는 2번만 하면 됨
            if arr[i+k][j]!=arr[i+5-k-1][j]:
                break
        # for ~ else 구문 기억하기 !!!
        else:
            cnt+=1
print(cnt)

'''# 내 답안 - 제대로 나옴 (채점은 오류...)
def Check(arr):
    total=0 # 회문수
    for i in range(7):
        for j in range(3):
            num = j+j+4
            cnt1=0
            cnt2=0
            for k in range(2):
                if(arr[i][j+k]==arr[i][num-(j+k)]):
                    cnt1+=1
                if(arr[j+k][i]==arr[num-(j+k)][i]):
                    cnt2+=1
            if(cnt1==2):
                total+=1
            if(cnt2==2):
                total+=1
    return total

print(Check(arr))'''