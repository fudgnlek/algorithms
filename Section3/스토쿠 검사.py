import sys
# sys.stdin = open("input.txt","rt")

a = [list(map(int,input().split())) for _ in range(9)]

'''
각 행, 열 검사 코드는 각 행,열을 뽑아내서 정렬해서 1~9 배열과 똑같은지를 검사하는 형태로 
했는데 그렇게 하면 뒤에 3x3 검사할 때 정렬된 배열로 인해 제대로 동작을 안해서
강의에서 설명한 ch 배열을 두고 합을 검사하는 형태로 수정함
'''
def check(a):
    for i in range(9):
        ch1 = [0]*10
        ch2 = [0]*10
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False

    # 3X3 검사하는 방법은 해결 못해서 강의 참고함
    for i in range(3):
        for j in range(3):
            ch3 = [0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1 # i와 k가 행을 맡고 j와 s가 열을 맡음
            if sum(ch3)!=9:
                return False
    return True

if check(a):
    print("YES")
else:
    print("NO")