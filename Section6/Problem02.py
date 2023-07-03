# 전역변수와 지역변수

def DFS():
    global a
    a = a+[4] # 이런 경우 error 발생 (a라는 리스트가 선언되지 않았기 때문 - 로컬 리스트) -> global 사용하여 전역 리스트 사용
    #a[0]=7 # 새로운 리스트 생성이 아니라 a라는 리스트이 0번 인덱스 값을 7로 변경한다는 뜻 (전역 리스트로 인식)
    # a =  [7,8] # 이런 경우 a=이기때문에 a라는 새로운 리스트 생성 (로컬 리스트)
    print(a)

def DFS1():
    cnt=3 # 지역변수 cnt 생성
    print(cnt) 
    # cnt가 자신의 지역변수인지를 먼저 확인 (함수는 지역변수가 우선) 
    # 없다면 전역변수인가를 확인
    # 전역변수도 없다면 error 발생


def DFS2():
    global cnt # 밑의 cnt를 지역변수로 선언 안함 (전역변수로 작동 - 해당 함수 내에서)
    if cnt==5:
        cnt= cnt+1 # 위의 선언을 하지 않았을 경우 지역변수 cnt 생성 (하지만 지역변수 cnt 값 자체가 생성이 안됨 -> error 발생)
        print(cnt)
    
if __name__=="__main__":
    cnt=5 # 전역변수
    a = [1,2,3]
    DFS1()
    DFS2()
    print(cnt)
    DFS()
    print(a)
    