# 순서가 있는 값들의 모음을 시퀀스라고 한다. for문은 시퀀스를 사용해서 반복한다. a에는 배열(list)의 값이 하나씩 차례대로 대입된다.
for i in [1,2,3,4,5] : 
    print(i) #인덴트에 따라 반복할 명령이 정해진다. 이 때문에 인덴트가 파이썬에서 중요한 것이다.

# range(시작하는 값, 종료하는 값)는 시작하는 값부터 종료하는 값 -1 까지 연속된 값의 시퀀스를 만들어준다. range의 0은 생략해도 된다.
for i in range(0,100) : 
    print(i)

for i in "Hello" :
    print(i)

total = 0
a = 1
while total <= 50 :
    total += a
    a += 1
print(total)

# python에선 반복문을 종료할 때 반드시 실행되는 else라는 부분을 작성할 수 있다. for문이나 while문이 끝났을 때 특정 명령을 실행하고 싶다면 else를 사용하면 된다.
for i in range(5):
    print(i)
else: 
    print("반복을 종료합니다.")

# python에선 논리연산자가 and, or, not이다. 다른 프로그래밍 언어들은 & | ! 기호를 쓰는데 비해 더 직관적이다.
for a in range(10):
    if a > 3 and a < 8 :
        print("3초과 8미만")

# elif를 사용해 조건분기를 보기 편하게 할 수 있다.
a = 5
if a < 5:
    print("5미만")
elif 5 <= a and a <= 9:
    print("5이상 9이하")
else:
    print("9초과")

# python에는 '아무것도 하지 않는 문'이 있다. 아무것도 하지 않을 때 그냥 공백으로 둔다면 에러가 발생한다. 따라서 pass를 작성해서 아무것도 하지 않음을 프로그램에 알려야한다.
a = 3
if a == 3:
    pass

# 함수 내에서 전역변수의 값을 변경, 사용하고 싶을 땐 global이라는 식별자를 써주면 된다.
a = "abc"
def test():
    global a
    a = "def"
    print(a)
test()
print(a)

# 파이썬은 '기본 기능은 간단하고, 응용적인 기능은 모듈이 갖고 있다'는 설계 철학을 갖고있다. 따라서 추가적인 기능을 사용하고 싶다면 module(모듈)을 읽어야 하는데, 그 동작을 import한다고 말한다.
import calendar as c # as를 사용해 모듈의 별칭을 지을 수 있다.
print(c.month(2023,10))

# from을 사용해서 모듈명을 사용하지 않고 함수명만 사용할 수 있다. 해당 모듈에서 특정 함수만 가져와 사용할 때 유용하다.
from calendar import month
print(month(2023,10))