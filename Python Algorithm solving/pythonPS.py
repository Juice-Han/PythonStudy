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

#PS-13 OX퀴즈

# result = "OOOOXOOOOXOOOOX"

# def solution(result):
#     count = 0
#     Sum = 0
#     for i in result:
#         if i == "O":
#             count += 1
#             Sum += count
#         else:
#             count = 0
#     return Sum
# print(solution(result))

#PS-14 숫자의 개수

# A = 150
# B = 266
# C = 427

# def solution(A,B,C):
#     arr = [0 for _ in range(10)]
#     # mul = str(A*B*C) #내가 푼 방법
#     # for i in range(10):
#     #     for num in mul:
#     #         if int(num) == i:
#     #             arr[i] += 1
    
#     num = A*B*C # 해답에 나온 풀이 <- 해당 숫자와 인덱스가 같다는 걸 잘 활용하여 코드를 간단하게 만듦
#     while num > 0:
#         arr[num%10] += 1
#         num //= 10
#     return arr
        
# print(solution(A,B,C))

#PS-15

# n = 10

# def solution(n):
#     ans = ""
    
#     # while n > 0:
#     #     n -= 1
#     #     if n%3 == 0:
#     #         ans += '1'
#     #     elif n % 3 == 1:
#     #         ans += '2'
#     #     else:
#     #         ans += '4'
#     #     n //= 3
#     # return ans[::-1]
    
#     while n > 0:    
#         n -= 1
#         v = n % 3
#         if v == 0:
#             ans += '1'
#         elif v == 1:
#             ans += '2'
#         else:
#             ans += '4'
#         n = n // 3
#     return ans[::-1]
        

# print(solution(n))

#PS-16 손익분기점

# A = 1000
# B = 70
# C = 170

# def solution(A,B,C):
#     if (C-B) < 0:
#         return -1
#     ans = A//(C-B) + 1
#     return ans

# print(solution(A,B,C))    

#PS-17 큰 수 A+B

# def solution(A,B):
#     ans = ""
#     A = A[::-1]
#     B = B[::-1]
#     if len(A) > len(B):
#         C = A
#         A = B
#         B = C
    
#     c = 0

#     for i in range(len(A)):
#         ans += str((int(A[i]) + int(B[i]) + c)%10)
#         c = (int(A[i]) + int(B[i]) + c) // 10
    
#     for i in range(len(A),len(B)):
#         ans += str((int(B[i]) + c )% 10)
#         c = (int(B[i]) + c) // 10
    
#     if c == 1:
#         ans += '1'
    
#     return ans[::-1]

    

# A = "9223372036854775807"
# B = "9223372036854775808"
# print(solution(A,B))

#PS-18 

# n = 58
# def solution(n):
#     count = 1
#     pl = 6
#     while n > 1: 
#         n -= pl
#         count += 1
#         pl *= 2
#     return count

# print(solution(n))

#PS-19

# n = 500
# lists = [93,181,245,214,315,36,185,216,295]

# def solution(n,lists):
#     maxsum = 0
#     for i in range(1,len(lists)-2):
#         for j in range(i+1, len(lists)-1):
#             for k in range(i+2, len(lists)):
#                 Sum = lists[i]+lists[j]+lists[k]
#                 if (Sum > maxsum) and (Sum <= n):
#                     maxsum = Sum
#     return maxsum

# print(solution(n,lists))

#PS-20

# nums = [7,5,11,13,1,3]

# def solution(nums):
#     count = 0
#     for n in nums:
#         for i in range(len(nums)):
#             if nums[i] == n*2:
#                 count += 1
#     return count

# print(solution(nums))

#PS-21

# dwarfs = [8,6,5,1,37,30,28,22,36]
# def solution(dwarfs):
#     Sum = sum(dwarfs)
#     for i in range(len(dwarfs)-1):
#         for j in range(i+1,len(dwarfs)):
#             if (Sum - dwarfs[i] - dwarfs[j]) == 100:
#                 dwarfs.remove(dwarfs[j])
#                 dwarfs.remove(dwarfs[i])
#                 return dwarfs

# print(solution(dwarfs))

#PS-22

# N = 216

# def solution(N):
#     for i in range(N):
#         num = str(i)
#         Sum = i
#         for n in num:
#             Sum += int(n)
#         if Sum == N:
#             return i
#     return 0            

# print(solution(N))

#PS-23

# people = [[55,185], [58,183], [88,186], [60,175], [46,155]]

# def solution(people):
#     # length = len(people) #내가 푼 풀이
#     # grade = [1 for _ in range(length)]
#     # for a in range(length-1):
#     #     for b in range(a+1,length):
#     #         if (people[a][0] < people[b][0]) and (people[a][1] < people[b][1]):
#     #             grade[a] += 1
#     #         elif (people[a][0] > people[b][0]) and (people[a][1] > people[b][1]):
#     #             grade[b] += 1

#     grade = []
#     for person in people:
#         rank = 1
#         for compare in people:
#             if person[0] < compare[0] and person[1] < compare[1]:
#                 rank += 1
#         grade.append(rank)
#     return grade

# print(solution(people))

#PS-24

# board = ["BBBBBBBBWBWBW", "BBBBBBBBBWBWB", "BBBBBBBBWBWBW", "BBBBBBBBBWBWB", "BBBBBBBBWBWBW", "BBBBBBBBBWBWB", "BBBBBBBBWBWBW", "BBBBBBBBBWBWB", "WWWWWWWWWWBWB", "WWWWWWWWWWBWB"]

# def check(board):
#     ans1 = 64
#     ans2 = 64

#     board1 = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]
#     board2 = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW","WBWBWBWB"]

#     for i in range(8):
#         for j in range(8):
            
#             if board1[i][j] != board[i][j]:
#                 ans1 -= 1
#             if board2[i][j] != board[i][j]:
#                 ans2 -= 1
    
#     return min(ans1,ans2)


# def solution(board):
#     ans = 64
#     n = len(board)
#     m = len(board[0])
#     for i in range(n-7):
#         for j in range(m-7):
#             temp=[]
#             for k in range(8):
#                 temp.append(board[i+k][j:j+8]) # 2차월 배열에 이중 슬라이싱은 불가하다
#             ans = min(ans,check(temp))
#     return ans

# print(solution(board))

#PS-25 피보나치 수

# def solution(n):
#     if n < 2:
#         return n
#     return solution(n-1) + solution(n-2)

# n = 15
# print(solution(n))

#PS-26

# def solution(n):
#     if n == 1:
#         return 1
#     return n * solution(n-1)

# n = 10
# print(solution(n))

#PS-27 하노이탑 옮기기
# def solve(n, From, To):
#     ans = 0
#     if n == 0:
#         return 0
#     ans += solve(n-1,From,6-From-To)
#     print(From,To)
#     ans += solve(n-1,6-From-To,To)
#     return ans

# def solution(n):
#     return solve(n,1,3)

# n = 5
# solution(n)

#PS-28 부분수열의 합
# s = 0
# nums = [-7, -2, -3, 8, 6]
# count = 0

# def solve(Sum,nums,s,n):
#     global count
#     if n == len(nums):
#         return
#     if Sum + nums[n] == s:
#         count+=1
#     solve(Sum+nums[n],nums,s,n-1)
#     solve(Sum,nums,s,n-1)

# def solution(nums,s):
#     solve(0,nums,s,0)

# solution(nums,s)
# print(count)

#PS-29
# ans = [] # 내가 푼 해답
# S = [1,2,3,5,8,13,21,34]
# def solution(S,n):
#     global ans
#     if len(S) == 6:
#         ans.append(S)
#         return
#     if n < 0:
#         return
#     tmp = S[:]
#     tmp.remove(S[n])
#     solution(tmp,n-1)
#     solution(S,n-1)
# solution(S,len(S)-1)
# print(ans)
# ans = [] # 해설지에 적힌 해답
# def solve(s,n,k):
#     if len(k)==6:
#         ans.append([])
#         for num in k:
#             ans[-1].append(num)
    
#     for i in range(n,len(s)):
#         k.append(i)
#         solve(s,n+1,k)
#         del k[-1]

# def solution(s):
#     solve(s,0,[])
#     return ans

#PS-30
# values=[] # 내가 푼 풀이
# energies = [1,2,3,4]

# def solve(energies,total):
#     global values
#     length = len(energies)
#     if length == 2:
#         values.append(total)
#         return
#     for i in range(1,length-1):
#         tmp_energies = energies[:]
#         tmp_total = total + (energies[i-1]*energies[i+1])
#         tmp_energies.remove(energies[i])
#         solve(tmp_energies,tmp_total)
# def solution(energies):
#     solve(energies,0)

# solution(energies)
# print(max(values))

# energies = [1,2,3,4] 해답지 풀이 : 전역변수를 사용하지 않고 요소를 뺏다가 재귀함수 호출하고 요소를 다시 넣는 방법으로 최댓값을 구했다.
# def solve(energies, total):
#     if len(energies) <= 2:
#         return total
    
#     ans = 0

#     for i in range(1, len(energies) -1):
#         temp = energies[i]
#         del energies[i]
#         ans = max(ans,solve(energies,total+energies[i-1]*energies[i]))
#         energies.insert(i,temp)
    
#     return ans

# def solution(energies):
#     return solve(energies,0)

# print(solution(energies))

#PS-31

# results = []
# nums = [1,2,3,4,5,6]
# operators = [3,2,1,1]

# def solve(nums,operators,total):
#     global results
#     if len(nums) == 0:
#         results.append(total)
#         return
#     for i in range(len(operators)):
#         if operators[i] == 0:
#             continue
#         operators[i] -= 1
#         tmp = nums[0]
#         del nums[0]
        
#         if i == 0:
#             solve(nums,operators,total+tmp)
#         elif i == 1:
#             solve(nums,operators,total-tmp)
#         elif i == 2:
#             solve(nums,operators,total*tmp)
#         else:
#             if total < 0:
#                 solve(nums,operators,((-1)*total//tmp)*(-1))
#             else:
#                 solve(nums,operators,total//tmp)
#         nums.insert(0,tmp)
#         operators[i] += 1

# def solution(nums,operators):
#     total = nums[0]
#     del nums[0]
#     solve(nums,operators,total)

# solution(nums,operators)
# print(max(results),min(results))

#PS-32
# board = "dcdd"

# def solve(board,n):
#     if len(board) == n:
#         return 1
#     if board[n] == 'd':
#         if n > 0 and board[n-1] == 'd':
#             return 9*solve(board,n+1)
#         else:
#             return 10*solve(board,n+1)    
#     else:
#         if n > 0 and board[n-1] == 'c':
#             return 25*solve(board,n+1)
#         else:
#             return 26*solve(board,n+1)
        
# def solution(board):
#     return solve(board,0)

# print(solution(board))

# cos pro 1급 3차시 5번
# def bishop_int(bishop):
#     x = ord(bishop[0]) +1 -65
#     y = int(bishop[1])
#     return (x,y)

# def bishop_move(bishop):
#     result = set()
#     x, y = bishop_int(bishop)
#     b_up = y - x
#     b_down = y + x

#     for i in range(1,9):
#         if 0 < i+b_up < 9:
#             result.add((i,i+b_up))
#         if 0 < -i+b_down < 9:
#             result.add((i,-i+b_down))

#     return result

# def solution(bishops):
#     result = set([bishop_int(bishop) for bishop in bishops])
#     for bishop in bishops:
#         result |= bishop_move(bishop)
#     return 64 - len(result)

# print(solution(["D5"]))
# print(solution(["D5","E8","G2"]))

# cos pro 1급 3차시 4번
# def counting(s1,s2):
#     count = 0
#     for i in range(1,min(len(s1),len(s2))+1):
#         tmp1 = s1[-i::1]
#         tmp2 = s2[0:i]
#         if tmp1 == tmp2:
#             count = i
#     return len(s1)+len(s2)-count

# def sol(s1, s2):
#     result = [counting(s1,s2), counting(s2,s1)]
#     return min(result)

# print(sol("ababcd","abcdab"))

#cos pro 1급 3차시 5번

# def solution(phrases, second):
#     answer = ''
#     display = '______________' + phrases
#     for i in range(second):
#         display = display[1:] + display[0]
#     answer = display[:14]
#     return answer
# phrases = "happy-birthday"
# second = 3
# print("solution 함수의 반환 값은 ", solution(phrases, second), "입니다.")

# cos pro 1급 5차시 2번

# def solution(walls):
#     answer = 0
#     for i in range(len(walls)):
#         for j in range(i+1, len(walls)):
#             area = 0
#             if walls[i][1] < walls[j][1]:
#                 area = walls[i][1] * (walls[j][0] - walls[i][0])
#             else:
#                 area = walls[j][1] * (walls[j][0] - walls[i][0])
#             if answer < area:
#                 answer = area
#     return answer

# walls = [[1,4], [2, 6], [3, 5], [5,3], [6,2]]
# ret = solution(walls)

# print("solution 함수의 반환 값은 ", ret, "입니다.")

# cos pro 1급 5차시 9번
# import queue
# def solution(number, target):
#     answer = 0
#     visited = [0 for _ in range(10001)]
#     q = queue.Queue()
#     q.put(number)
#     visited[number] = 1
#     while not q.empty():
#         x = q.get()
#         if x == target:
#             break
#         if x+1 <= 10000 and visited[x+1] == 0:
#             visited[x+1] = visited[x]+1
#             q.put(x+1)
#         if x-1 >= 0 and visited[x-1] == 0:
#             visited[x-1] = visited[x]+1
#             q.put(x-1)
#         if 2*x <= 10000 and visited[2*x] == 0:
#             visited[2*x] = visited[x]+1
#             q.put(2*x)
#     answer = visited[target] -1 
#     return answer

# number1 = 5
# target1 = 9
# ret1 = solution(number1, target1)

# print("solution 함수의 반환 값은 ", ret1, "입니다.")

# number2 = 3
# target2 = 11
# ret2 = solution(number2, target2)

# print("solution 함수의 반환 값은 ", ret2, "입니다.")
