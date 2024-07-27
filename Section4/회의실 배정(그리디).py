import sys
sys.stdin = open("input.txt","rt")

n = int(input())
room = []
for i in range(n):
    s,e = map(int,input().split())
    room.append((s,e))
''' 답안 참고
시작 시간이 빠르다고 해서 중요한게 아니라
빨리 끝나는게 중요함 그래야 회의갯수를 많이 할 수 있으니까
'''
room.sort(key=lambda x:(x[1],x[0]))
fin = room[0][1]
cnt = 1
for i in range(1,n):
    if fin <= room[i][0]:
        fin = room[i][1]
        cnt += 1
print(cnt)