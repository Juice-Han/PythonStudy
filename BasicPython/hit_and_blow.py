import random
# import re

a = [random.randint(0,9),
    random.randint(0,9),
    random.randint(0,9),
    random.randint(0,9)]

isOk = False # 반복을 할지 말지를 판정하기 위해 True나 False 값을 갖는 변수를 플래그라고 한다.

while isOk == False :
    b = input("숫자를 입력하세요> ") #파이썬에서 input으로 입력받은 값은 문자열이다. 문자열을 정수로 바꾸고 싶다면 int함수를 사용하자.
    if len(b) != 4:
        print("네 자릿수의 숫자를 입력하세요")
    else:
        numberOk = True
        for i in range(4):
            if b[i] < "0" or b[i] > "9":
                print("숫자가 아닙니다.")
                numberOk = False
                break
        if numberOk:
            isOk = True
    # if not re.match(r"^\d\d\d\d$",b): # re모듈에서 정규표현식을 활용한 검사를 하면 훨씬 간단하게 입력받은 값을 검사할 수 있다.
    #     print("네 자릿수의 숫자를 입력하세요")
    # else:
    #     isOk = True    

hit = 0
blow = 0
for i in range(4):
    if int(b[i]) == a[i]: # b[i]는 문자열이므로 숫자와 비교하기 위해 정수로 바꿔줘야 한다.
        hit += 1
for i in range(4):
    if int(b[0]) == a[i]:
        blow += 1
        break

if a == b :
    print("맞췄음")
else:
    print("틀렸음")