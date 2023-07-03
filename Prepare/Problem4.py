# 최솟값 구하기
arr = [5,3,7,9,2,5,6]
arrMin = float('inf') # 파이썬에서 가장 큰 값이 저장됨 (초기화)
# arrMin = arr[0] # 이렇게 해도 됨
for i in range(len(arr)):
    if arr[i]<arrMin: # <= (위치도 중요하다면 같다도 추가해줘야함)
        arrMin=arr[i] 
print(arrMin)

# 이런식으로도 가능
for x in arr:
    if x<arrMin:
        arrMin=x
print(arrMin)

# 대표값 (딕셔너리로 풀려고 했는데 못품 - enumerate 함수 배움)

import sys
sys.stdin = open("input.txt","rt")

n = int(input()) # 학생 수
grade = list(map(int,input().split()))

# 평균 구하기
average = 0
for x in grade:
    average += x

average = average/len(grade)
# average = round(average)
# round X, 소수점 첫째자리 반올림할 때는 이 방법 쓰기 !
average = average+0.5
average = int(average) 

# 답안 - 평균 구하기
ave = round(sum(grade)/n)

# 답안 계속
min = 2147000000 # 정수형 가장 큰 값
for idx,x in enumerate(grade): # enumerate는 리스트의 index값과 value값을 쌍으로 대응해주는 함수
    temp = abs(x-average)
    if(temp < min):
        min = temp
        score = x
        res = idx+1
    elif(temp==min):
        if(x>score): # >= 로 해버리면 학생번호가 더 늦은 학생이 출력됨 
            score = x
            res = idx+1
print("{0} {1}".format(average,res))

# 대표값 문제 오류 수정
# round는 round_half_even 방식 (정확한 half일 경우 짝수쪽으로 감)
a = 4.5
print(round(a)) # 이렇게 하면 4,5 중에 짝수인 4로 내림
# 4.51 뭐 이럴경우엔 상관없는데 정확한 half일 경우 문제가 생김 -> 이 경우 때문에 round 쓰면 안됨 !

# 소수점 첫째자리에서 반올림 할 때는 아래 방법 처럼 0.5를 더하고 int형으로 바꿔주기
a = 66.5
a = a + 0.5
a = int(a)
print(a)

