# 가방문제 (냅색 알고리즘)
import sys
# sys.stdin=open("input.txt","r")
input=sys.stdin.readline

# 강의듣고 코드 작성 (맞음)
n,m=map(int,input().split())
# 이 경우 최댓값을 먼저 입력받기 때문에 배열 굳이 안만들고
# 밑의 for문 중간에서 입력 하나씩 받아도 됨
a=[list(map(int,input().split()))for _ in range(n)]
dy=[0]*(m+1)

for i in range(n):
    for j in range(a[i][0],m+1):
        dy[j]=max(dy[j-a[i][0]]+a[i][1],dy[j])

print(dy[m])

# Feedback
# 한 종류 여러개 담을 수 있음 -> dy배열 생성
'''
<냅색 알고리즘>
dy[i] : 가방에 jkg까지 담을 수 있을 때 최대가치
최댓값을 구하는 것이므로 dy배열 0으로 초기화
dy[j-w]+v : w만큼은 무조건 담는다는 가정이므로 지정된 최대무게에서 w만큼은 여유공간을
남겨두고 나머지에서 최대무게 + w를 담았을 때 가치 v

j가 w부터 쭉 움직이면서 dy table 값 할당 -> 한 종류가 여러개 있을 수 있으니까
w가 다른 값으로 바뀌었을 때 값이 겹친다면 ?
두 값 중 최댓값으로 변경
'''


'''원래 내 답안 - 한 종류 여러개 가능하다는 점 고려 못함
def dfs(k,p,l):
    global maxx
    if l==n:
        return
    if k+a[l][0]>11:
        if maxx<p:
            maxx=p
        return    
    else:
        dfs(k+a[l][0],p+a[l][1],l+1) # 저장한 경우
        dfs(k,p,l+1) # 저장하지 않은 경우
if __name__=="__main__":
    n,m=map(int,input().split())
    a=[list(map(int,input().split()))for _ in range(n)]
    maxx=-2147000
    dfs(0,0,0)
    print(maxx)'''
