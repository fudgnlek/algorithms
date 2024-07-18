# 람다함수 = 익명의 함수, 표현식 등

# 그냥 함수
def plus1(x):
    return x+1
print(plus1(1))

# 람다함수
plus2 = lambda x:x+2 # plus2는 변수
print(plus2(1))

# 유용한 경우 - 내장함수의 인자로 활용
a= [1,2,3]
print(list(map(plus1,a))) # map(함수명, 자료)

print(list(map(lambda x:x+1,a))) # 위의 코드와 같은 기능 (그렇지만 함수 따로 필요 없다는 장점)
