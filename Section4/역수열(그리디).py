import sys
# sys.stdin = open("input.txt","rt")
'''
내 답안 맞음
근데 강의 답안과 다른 코드
- 강의 코드 원리 이해 필요 (강의 참고)
'''

n = int(input())
a = list(map(int,input().split()))
tmp = []
for idx,x in enumerate(a):
    tmp.append((idx+1,x))
tmp.sort(key=lambda x:(x[1],-x[0]))
res = [tmp[0][0]] # 출력할 배열

for i in range(1,n):
    n = tmp[i][0] # 숫자
    loc = tmp[i][1] # 앞에 있는 큰 수 갯수
    cnt = 0
    if loc == 0: # 숫자를 내림차순 해놨기 때문에 역수열 값이 0이라면 계속 맨 앞에 추가하면 됨됨
        res.insert(0,n)
        continue    
    for j in range(len(res)):
        if res[j] > n:
            cnt += 1
        if loc == cnt:
            res.insert(j+1,n)
            break
for x in res:
    print(x,end=' ')