# 스토쿠 검사

import sys
sys.stdin = open("input.txt","rt")

# 답안 참고 - 행,열은 내가 짜고 그룹은 못함
def Check(arr):
    for i in range(9):
        ch1 = [0]*10 # 행
        ch2 = [0]*10 # 열
        for j in range(9):
            ch1[arr[i][j]]=1
            ch2[arr[j][i]]=1
        if sum(ch1)!=9:
            return False
        if sum(ch2)!=9:
            return False
    # 그룹 check
    for i in range(3):
        for j in range(3): # 여기까지는 그룹설정 (총 9번)
            ch3 = [0]*10 # 그룹
            for k in range(3): # 여기부분은 그룹 안에서 탐색
                for s in range(3):
                    ch3[arr[i*3+k][j*3+s]]=1
            if(sum(ch3)!=9):
                return False
            
    return True

arr = [list(map(int,input().split())) for _ in range(9)]
if Check(arr):
    print("YES")
else:
    print("NO")
    



