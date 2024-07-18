import sys
sys.stdin = open("input.txt","rt")

n,m = map(int,input().split())
arr = list(map(int,input().split()))

'''
정확성도 보지만 효율성도 본다고 문제에서 미리 이야기해주는 경향이 많음
N 제한이 보통 십만 이상으로 주어지면 효율성도 본다고 생각하면 됨
그것도 아니면 채점해보고 판단해야함

이 문제의 경우 O(n)의 시간복잡도로 풀어야 함
>> 시간복잡도 계산하고 문제에 따라 어떤 시간복잡도까지 괜찮은지 판단하는 방법 공부 필요
'''

# 답안
lt = 0
rt = 1
tot = arr[0] # tot는 lt부터 rt 바로 전 값까지의 합을 의미
cnt = 0

while True:
    if tot<m:
        if rt<n:
            tot+=arr[rt]
            rt+=1
        else: # m보다 작은데 더 더할 값은 없는 경우
            break
    elif tot==m:
        cnt+=1
        tot-=arr[lt]
        lt+=1
    else:
        tot-=arr[lt]
        lt+=1

print(cnt)

'''# 내 답안 (출력값은 맞는데 마지막 테케가 시간초과 발생)
cnt = 0 # 답 (경우의 수)
for i in range(n):
    sum = 0
    for  j in range(i,n):
        if sum+arr[j] == m:
            # print(i,j)
            cnt += 1
            break
        elif sum+arr[j] > m:
            break
        else:
            sum+=arr[j]
print(cnt)'''
