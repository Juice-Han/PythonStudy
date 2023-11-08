#세 정수를 입력받아 최댓값 구하기
# print("세 정수의 최댓값을 입력합니다.")
# a = int(input('정수 a의 값을 입력하세요: '))
# b = int(input('정수 b의 값을 입력하세요: '))
# c = int(input('정수 c의 값을 입력하세요: '))

# maximum = a

# if maximum < b : maximum = b
# if maximum < c : maximum = c

# print(f'최댓값은 {maximum}입니다.') # f-string 문자열 포맷

#정수형 형변환
# int('0b10110',2) # 2진수 -> 정수
# int('0o75',8) # 8진수 -> 정수
# int('0xA23F',16) # 16진수 -> 정수

# 세 정수를 입력받아 최댓값 구하기를 함수로 표현
# def max3(a,b,c):
#     """a, b, c의 최댓값을 구하여 반환"""
#     maximum = a
#     if b > maximum : maximum = b
#     if c > maximum : maximum = c
#     return maximum

# print(f'max3(3,2,1) = {max3(3,2,1)}')
# print(f'max3(3,1,2) = {max3(3,1,2)}')
# print(f'max3(2,1,3) = {max3(2,1,3)}')

# 세 정수를 입력받아 중앙값 구하기 1

# def med3(a, b, c):
#     if a >= b:
#         if b >= c:
#             return b
#         elif c >= a:
#             return a
#         else:
#             return c
#     elif a > c:
#         return a
#     elif b > c:
#         return c
#     else:
#         return b

# print('세 정수의 중앙값을 구합니다.')
# a = int(input('정수 a의 값을 입력하세요: '))
# b = int(input('정수 b의 값을 입력하세요: '))
# c = int(input('정수 c의 값을 입력하세요: '))
# print(f'중앙값은 {med3(a,b,c)}입니다.')

#삼항 연산자 if~else 문
# x = 2
# y = 1
# a = x if x > y else y
# print(a)
#문자열에도 적용가능
# c = 1
# print('c는 0 입니다.' if c == 0 else 'c는 0이 아닙니다.')

