# 알파코드 (DFS)

import sys
# sys.stdin = open("input.txt","rt")

# 답안 - 제대로 그려가면서 다시 봐야할듯
def DFS(L,p):
    global cnt
    if L==n: # 종착점에 도착
        cnt+=1
        for j in range(p):
            # 알파벳으로 바꿔주기 위해 chr을 사용하고 대문자로 표현하기 위해 64를 더해줌
            print(chr(res[j]+64),end='')
        print()
    else:
        for i in range(1,27): # 26가닥 뻗기
            if code[L]==i: # 한자리 숫자
                res[p]=i
                DFS(L+1,p+1) # 한자리니까 L+1 (p는 인덱스니까 무조건 +1)
            # 두자리 숫자이고 만약에 i가 23이면 첫번째는 10으로 나눈 몫(2), 두번째는 10으로 나눈 나머지(3)와 같아야함
            elif i>=10 and code[L]==i//10 and code[L+1]==i%10: 
                res[p]=i
                DFS(L+2,p+1) # 두자리 숫자니까 L+2

if __name__=="__main__":
    code = list(map(int,input())) # 리스트로 입력받음
    n=len(code)
    code.insert(n,-1) # 비교할때 L,L+1 이렇게 하니까 out of index 오류를 막기 위해서 맨 마지막에 -1을 넣어둠 (참은 되지 않지만 오류 발생도 막음)
    res=[0]*(n+3)
    cnt=0
    DFS(0,0)
    print(cnt)