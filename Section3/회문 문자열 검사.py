import sys
sys.stdin = open("input.txt","rt")

n = int(input())
for i in range(n):
    word = str(input()).upper() 
    # word = input() # 답안에서는 굳이 str() 안해줌 type 확인해보니까 이렇게만 해도 str임
    length = len(word)
    '''
    if s == s[::-1]: 이렇게 뒤집는 걸로 활용
    이 생각까지 못함 이제 하자 !    
    '''
    for j in range(0,length//2):
        # print(j)
        if word[j] != word[length-j-1]: # 회문 문자열 아님
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))