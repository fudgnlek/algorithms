# K번째 수

import sys
# sys.stdin=open("input.txt","rt")

n = int(input()) # case 개수

# 나는 range(1,n+1)로 했는데 range(n)으로 해도 되는건가 ?
# range(n)하면 범위 어떤식으로 되는거지
for i in range(n):
    N,s,e,k = map(int,input().split())
    num = list(map(int,input().split()))
    # print(num)
    print("#{0}".format(i+1),end=" ")
    num2 = num[s-1:e]
    num2.sort()
    print(num2[k-1])

# 답안 (출력문만 다름)
#print("#%d %d" %(n+1,num2[k-1]))