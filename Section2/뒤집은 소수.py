import sys
# sys.stdin = open("input.txt","rt")

n = int(input())
num = list(map(int,input().split()))
def reverse(x):
    tmp = str(x)
    tmp = tmp[::-1]
    return int(tmp)
'''# 답안은 각 자릿수를 10을 나눈 나머지, 몫 등으로 구함 (강의 참고)
res = 0
while x>0:
    t=x%10 # x의 1의자리수
    res=res*10+t
    x=x//10
return res'''

def isPrime(x):
    ch = [0]*(x+1)
    ch[1] = 1
    for i in range(2,x+1):
        if ch[i]==0:
            for j in range(i*2,x+1,i):
                # print(j)
                ch[j]=1
    return ch[x]
'''# 답안
if x == 1:
    return False
for i in range(2,x//2+1): # 약수는 자기 자신을 제외하고는 절반까지 존재 (1x16 다음은 2x8 이니까)
    if x%i==0:
        return False
else: # for문이 정상적으로 종료되었다
    return True'''

for x in num:
    tmp = reverse(x)
    if not (isPrime(tmp)):
        print(tmp,end=' ')