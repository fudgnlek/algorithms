import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
num = list(map(int,input().split()))
answer = 0
result = []


def digit_sum(x):
    tmp = str(x)
    res = 0 # 각 숫자별 자릿수의 합
    for x in tmp:
        res += int(x)
    return res


for i in range(n):
    res = digit_sum(num[i])
    result.append((num[i],res))

result.sort(key=lambda x:(x[1]),reverse=True)
print(result[0][0])

# 답안은 digit_sum 함수 내용은 동일한데 그 후가 훨씬 깔끔
'''for x in a:
    tot = digit_sum(x)
    if tot>max:
        max=tot
        res=x'''

# 문제 이해를 잘못함 합이 같을 경우 다 출력하는줄 알고 길게 작성했는데
# 먼저 나온 수를 출력하는 것임을 이해하고 깔끔하게 수정 완료
# 답안은 max값을 주고 비교하는 코드, 나는 리스트를 정렬하는 코드