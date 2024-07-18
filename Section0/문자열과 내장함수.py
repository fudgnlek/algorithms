# 문자열과 내장함수

msg = "It is Time"
print(msg.upper()) # 모두 대문자로 (문자열 자체가 변한건 아님)
# x.isupper() x가 대문자인 경우 true 아닌 경우 false
print(msg.lower()) # 모두 소문자로
# x.islower() 마찬가지로 x가 소문자인지 확인

# x.isalpha() x가 알파벳인 경우 true (공백인 경우 false)

tmp = msg.upper()
print(tmp)
print(tmp.find('T')) # T가 있는 인덱스 번호를 출력
print(tmp.count('T')) # T가 몇개 있는지 출력
print(msg[:2]) # 2번 전까지 (0~1) 문자열 뽑아내서 출력
print(msg[3:5]) # 3~4 문자열 출력

tmp = 'AZ'
for x in tmp:
    print(ord(x)) # ord() x의 아스키넘버 출력 (A:65 ~ Z:90)

tmp = 65
print(chr(tmp)) # 아스키넘버를 대응되는 문자로 출력