# 뒤집은 소수

import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
num = list(map(int,input().split()))

'''# 답안
def reverse(x):
    res = 0 
    while x>0:
        t = x%10
        res = res*10+t
        x=x//10
    return res

def isPrime(x):
    if x==1: # 1은 소수가 아님
        return False
    for i in range(2,x//2+1): # 
        if x%i==0: # 약수가 존재함
            return False
    else:
        return True

for x in num:
    tmp = reverse(x)
    if isPrime(tmp): # 함수 리턴값이 True 인 경우가 소수인 경우니까 
        print(tmp,end=" ") '''

# 내 답안
def reverse(x): # 블로그 참고해서 한 것...
    rev = ''
    for x in str(x):
        rev = x + rev
    # print(int(rev))
    return int(rev)

    # a = len(str(x))
    # string = str(x)
    # for i in range(a):
    #     temp = string[i]
    #     string[i] = string[a-1-i]
    #     string[a-1-i] = temp
    # return int(string)

def isPrime(x):
    if(x!=1):
        cnt=1 # 1을 포함
        for i in range(2,x):
            if(x%i==0):
                cnt+=1
        if(cnt==1):
            print(x,end=" ")

for x in num:
    isPrime(reverse(x)) 
