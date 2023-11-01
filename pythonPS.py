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

#PS-8 10부제 차량 위반 차량 수 세기
# n = 1
# cars = [1,3,0,6,4]
# def solution(num, cars):
#     count = 0
#     for car in cars:
#         if num == car:
#             count += 1
#     return count
# print(solution(5,cars))

#PS-9 가장 높은 점수와 낮은 점수의 차 구하기
# scores = [85,42,79,95,37,11,72,32]
# def solution(scores):
#     Max = scores[0]
#     Min = scores[0]
#     for s in scores:
#         if s > Max:
#             Max = s
#         if s < Min:
#             Min = s
#     return Max-Min

# print(solution(scores))

#PS-10
# n = 18
# def solution(n):
#     # countArr = [] #내가 푼 방법 : 3킬로 봉지와 5킬로 봉지의 개수를 변수로 설정하고 모든 경우의 수를 구한 다음 최솟값을 리턴
#     # x_3 = 1
#     # while 3*x_3 <=n:
#     #     y_5 = 0
#     #     while (3*x_3 + 5*y_5) <= n:
#     #         if (3*x_3 + 5*y_5) == n:
#     #             countArr.append(x_3+y_5)
#     #             break
#     #         y_5 += 1
#     #     x_3 += 1
#     # if not countArr:
#     #     return -1
#     # return min(countArr)
#     ans = 0 # 정답 : 5킬로 봉지가 많을수록 봉지수가 줄어드니 전체 n에서 3씩 나눠주고 5로 나눠지면 해당 봉지 수 리턴
#     while n > 0:
#         if n % 5 == 0:
#             break
#         n -= 3
#         ans += 1
#     if n % 5 != 0:
#         ans = -1
#     else:
#         ans += n//5 # ans의 수는 3킬로 봉지수 n//5의 값은 5킬로 봉지수

#     return ans

# print(solution(n))

#PS-11 낮엔 a 높이만큼 올라가고 밤엔 b 높이만큼 내려가는 달팽이의 정상도착 일수 구하기
# a = 100
# b = 99
# v = 100000000
# def solution(a,b,v):
#     # height = 0 #반복문을 활용해서 구현
#     # count = 0
#     # while height < v:
#     #     count += 1
#     #     height += a
#     #     if(height >= v):
#     #         break
#     #     height -= b
#     #     print(count)
#     # return count
#     ans = 1 # 반복문을 사용하지 않고 구현
#     v -= a
#     if v > 0:
#         ans += v//(a-b)
#         if v%(a-b) > 0:
#             ans += 1
#     return ans

# print(solution(a,b,v))

#PS-12 더하기 싸이클
# N = 0

# def solution(N):
#     count = 1
#     newNum = (N%10)*10 + (N//10 + N%10)%10
#     while newNum != N :
#         newNum = (newNum%10)*10 + (newNum//10 + newNum%10)%10
#         count += 1
#     return count

# print(solution(N))