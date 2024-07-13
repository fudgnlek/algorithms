import sys
# sys.stdin = open("input.txt","rt")

n,k = map(int,input().split())
a = []
a.append(1)
a.append(n)

for x in range(2,n):
    if n%x == 0:
        tmp = n//x
        if tmp in a or x in a:
            break
        if tmp == x:
            a.append(x)
            continue
        a.append(x)
        a.append(tmp)

a.sort()
# print(a)
if len(a) < k:
    print(-1)
else:
    print(a[k-1])

# 풀긴 했는데 답안이 너무 간결함 (내 코드에 비해)
cnt = 0
for i in range(1,n+1):
    if n%i == 0:
        cnt+=1
    if cnt == k:
        print(i)
        break
else: # for문이 정상적으로 종료된 경우 (break문 실행 X)
    print(-1)

# 나는 약수를 구할 때 1,10 2,5 이렇게 짝을 함께 배열에 저장하려고 했는데
# 답안은 그냥 하나씩 구함 그래서 더 간결한듯