# PS-1 문자열 중간 출력하기
# a = input()
# n = len(a)
# if n % 2 == 0:
#     print(a[n//2-1:n//2+1]) 
# else:
#     print(a[n//2])

#PS-2 입력된 값 사이 값들의 총합 구하기
# a = int(input())
# b = int(input())
# sum = 0

# if a > b:
#     c = a
#     a = b
#     b = c

# for num in range(a,b+1):
#     sum += num

# print(sum)

#PS-3 입력된 수의 약수들의 총합 구하기
# n = int(input())
# sum = 0

# for num in range(1,n+1):
#     if n % num == 0:
#         sum += num

# print(sum)

#PS-4 피보나치 수열 항 구하기
# n = int(input())
# arr = [0,1]
# for i in range(1,n):
#     arr.append(arr[i] + arr[i-1])
# print(arr[n])

#PS-5 입력된 수들 중 홀수들의 함을 구하고 그 중 최솟값을 구하기
# oddArr = []
# Sum = 0

# for i in range(7):
#     n = int(input())
#     if n % 2 == 1:
#         oddArr.append(n)
#         Sum += n

# minOdd = oddArr[0]

# for odd in oddArr:
#     if minOdd > odd:
#         minOdd = odd

# print(str(Sum) + " " + str(minOdd))

#PS-6 1~4번 기차역에 내린사람 탄사람이 순서대로 입력될 때, 기차에 가장 많은 사람이 타 있을 때 사람 수는?
# Sum = 0
# Max = 0

# for i in range(4):
#     Sum -= int(input())
#     Sum += int(input())
#     if Max < Sum:
#         Max = Sum

# print(Max)

#PS-7 중앙의 노란색 타일의 수와 그걸 둘러싼 1줄의 갈색 타일의 수가 주어졌을 때 가로, 세로 길이 구하기
# brown = int(input())
# yellow = int(input())

# for i in range(1,yellow+1): #0으로 나눌 수 없음
    
#     if (yellow%i) == 0:
#         x = yellow//i
#         y = yellow//x
#         if x + y == (brown-4)//2 and x >= y:
#             print(x+2,y+2)
#             break
