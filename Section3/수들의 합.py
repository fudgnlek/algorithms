import sys
sys.stdin = open("input.txt","rt")

n,m = map(int,input().split())
arr = list(map(int,input().split()))

for i in range(n):
    sum = 0
    for  j in range(i,n):
        if sum+arr[j]:
