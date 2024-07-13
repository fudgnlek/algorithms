import sys
# sys.stdin = open("input.txt","rt")

t=int(input())

for case in range(t):
    n,s,e,k = map(int,input().split())
    a = list(map(int,input().split()))
    tmp = a[s-1:e]
    tmp.sort()

    print("#%d %d" %(case+1,tmp[k-1]))  