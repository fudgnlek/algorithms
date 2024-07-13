import sys
sys.stdin = open("input.txt","rt")

n = int(input())
num = list(map(int,input().split()))
def reverse(x):
    tmp = str(x)
    tmp = tmp[::-1]
    return int(tmp)

def isPrime(x):
    ch = [0]*(x+1)
    for i in range(2,x+1):
        if ch[i]==0:
            for j in range(i*2,x+1,i):
                # print(j)
                ch[j]=1
    return ch[x]

for x in num:
    tmp = reverse(x)
    if not (isPrime(tmp)):
        print(tmp,end=' ')