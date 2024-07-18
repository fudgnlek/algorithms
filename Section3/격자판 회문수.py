import sys
# sys.stdin = open("input.txt","rt")

def check(arr):
    if arr == arr[::-1]:
        return True
    else:
        return False

a = [list(map(int,input().split())) for _ in range(7)]
cnt = 0


'''
내 답안 (맞는지 틀린지 확인 X)
s=0
e=4
cnt = 0 # 총 회문수 출력

for i in range(7):
    row = a[i] # 행 단위
    tmp = row[s:e+1] # 5자리씩 확인
    if check(tmp): # 회문수인지 확인
        cnt += 1
    if e==6: # 한 행 검사 완료
        s=0
        e=4
        continue
    s+=1
    e+=1
'''


'''
답안 참고 - 열 부분 해결 못함
'''
for i in range(3): # 총 7자리라 5개씩 끊으려면 3번 반복함
    for j in range(7):
        row = a[j][i:i+5] # 행 부분
        if check(row):
            cnt+=1
        
        for k in range(2): # 열 부분
            # j는 고정되어 있다고 생각하고 회문수인지 확인 (중간에 있는 값 제외 2번 반복)
            # 근데 i+k와 i+5-k-1 어떻게 생각해내는지 모르겠음...
            if a[i+k][j]!=a[i+5-k-1][j]:
                break
        else:
            cnt+=1


print(cnt)