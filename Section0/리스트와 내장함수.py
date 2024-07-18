import random as r

# b = []
b = list(range(1,11))
print(b)

a = list(range(1,7))
a.insert(3,7) # 3번 인덱스로 7이 들어감 (나머지는 뒤로 밀림)

print(a.index(5)) # a 리스트에서 5라는 값의 인덱스 번호 출력

# 섞기
r.shuffle(a) # a를 무작위로 섞어봐라
print(a)
# 그래픽 게임 만들때 많이 씀

a.clear() # 빈 리스트 됨


# 리스트 값은 변경 가능하지만 튜플()은 값 변경 불가능

# enumerate
for x in enumerate(a):
    print(x[0],x[1])
    # x[0]은 index, x[1]은 값
    
if all(50>x for x in a): # 모든 값이 50보다 작아야 true
    print("YES")
else:
    print("NO")

if any(8<x for x in a): # 하나라도 8보다 크면 true
    print("YES")
else:
    print("NO")