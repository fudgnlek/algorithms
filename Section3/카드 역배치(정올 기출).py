import sys
# sys.stdin = open("input.txt","rt")

arr=[0]*(21)
for i in range(21):
    arr[i]=i
'''
답안은
a = list(range(21)) 이제 기억하자 !
'''

for i in range(10):
    a,b = map(int,input().split())
    '''
    for j in range((e-s+1)//2):
        a[s+j],a[e-j] = a[e-j],a[s+j]
    이해는 했는데 이런 공식을 어떻게 생각할지 ...
    '''
    tmp1 = arr[:a]
    target = arr[a:b+1]
    tmp2 = arr[b+1:]

    target = target[::-1] # 문자열 뒤집기
    arr = tmp1+target+tmp2



arr.pop(0) # 0 빼기
for x in arr:
    print(x,end=' ')