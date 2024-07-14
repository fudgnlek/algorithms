import sys
# sys.stdin = open("input.txt","rt")

n=int(input())
maxx = 0
for i in range(n):
    '''
    tmp = input().split() # 문자 형태로 저장됨 (리스트?)
    tmp.sort()
    a,b,c = map(int,tmp) # 이제 abc에 각 숫자로 저장됨
    '''
    arr = list(map(int,input().split()))
    arr.sort()
    if arr[0]==arr[1]==arr[2]: # 모두 같은 눈인 경우
        money = 10000+arr[0]*1000
    elif arr[0]==arr[1] or arr[1]==arr[2]: # 같은 눈 2개인 경우
        money = 1000+arr[1]*100
    else:
        money = arr[2]*100
    if maxx < money:
        maxx = money
print(maxx)