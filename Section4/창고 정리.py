import sys
# sys.stdin = open("input.txt","rt")

l = int(input())
a = list(map(int,input().split()))
m = int(input())
a.sort(reverse=True)
for _ in range(m):
    a[0] -= 1
    a[-1] += 1
    ''' 답안은 오름차순 정렬했고, 조건문 없이 계속 sort() 실행'''
    if a[0] < a[1] or a[-2] < a[-1]:
        a.sort(reverse=True)

print(a[0]-a[-1])

'''
max,min,index 함수는 리스트 전체를 탐색해야 하므로 O(n)
sort 함수는 대부분의 경우 O(nlogn)
그러므로 값의 양이 충분히 많아진다면 sort 사용하는 것이 더 효율적일 수 있음
but, l과 m값이 커진다면 매번 sort하는 코드도 시간초과 발생할 것
>> 리스트를 이용한 해시방법 추천 (코드 분석 필요)
'''