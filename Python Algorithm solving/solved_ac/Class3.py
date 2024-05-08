# 집합 11723번

# from sys import stdin, stdout
# def add(n_dict, x):
#     if n_dict[x] == None:
#         n_dict[x] = 1

# def remove(n_dict, x):
#     if n_dict[x] == 1:
#         n_dict[x] = None

# def check(n_dict, x):
#     if n_dict[x]:
#         stdout.write('1\n')
#     else:
#         stdout.write('0\n')

# def toggle(n_dict, x):
#     if n_dict[x] == 1:
#         n_dict[x] = None
#     else:
#         n_dict[x] = 1

# def all(n_dict):
#     for i in range(1,21):
#         n_dict[i] = 1

# def empty(n_dict):
#     for i in range(1,21):
#         n_dict[i] = 0

# N = int(stdin.readline())
# n_dict = dict.fromkeys([n for n in range(1,21)])
# for i in range(N):
#     op = stdin.readline().rstrip()
#     if op == 'all':
#         all(n_dict)
#     elif op == 'empty':
#         empty(n_dict)
#     else:
#         op, x = op.split()
#         if op == 'add':
#             add(n_dict, int(x))
#         elif op == 'remove':
#             remove(n_dict, int(x))
#         elif op == 'check':
#             check(n_dict, int(x))
#         else:
#             toggle(n_dict,int(x))

# 나는야 포켓몬 마스터 이다솜 1620번

# from sys import stdin, stdout
# N, M = map(int,stdin.readline().split())
# name2num_dict = dict()
# num2name_dict = dict()

# for i in range(1, N+1):
#     name = stdin.readline().rstrip()
#     name2num_dict[name] = i
#     num2name_dict[i] = name

# for i in range(M):
#     value = stdin.readline().rstrip()
#     if value.isalpha():
#         stdout.write(str(name2num_dict[value]) + '\n')
#     else:
#         stdout.write(num2name_dict[int(value)] + '\n')

# 듣보잡 1764번

# from sys import stdin, stdout
# N, M = map(int,stdin.readline().split())
# neverHeard = dict()
# neverSeen = []
# answer = []
# for i in range(N):
#     neverHeard[stdin.readline().rstrip()] = 1
# for i in range(M):
#     name = stdin.readline().rstrip()
#     if name in neverHeard:
#         answer.append(name)
# answer.sort()
# stdout.write(str(len(answer))+ '\n')
# for name in answer:
#     stdout.write(name + '\n')

# 동전 0 11047번

# from sys import stdin, stdout
# N, K = map(int,stdin.readline().split())
# count = 0
# val_list = []
# for i in range(N):
#     val_list.append(int(stdin.readline()))
# index = len(val_list) -1
# while index > -1:
#     div = K // val_list[index]
#     if div > 0:
#         K %= val_list[index]
#         count += div
#     if K == 0:
#         break
#     index -= 1
# stdout.write(str(count)+'\n')

# ATM 11399번

# from sys import stdin, stdout
# p_list = []
# N = int(stdin.readline())
# p_list = list(map(int,stdin.readline().split()))
# p_list.sort()
# for i in range(1,N):
#     p_list[i] += p_list[i-1]
# stdout.write(str(sum(p_list)) + '\n')

# 비밀번호 찾기 17219번

# from sys import stdin, stdout
# sitePwd = dict()
# N, M = map(int,stdin.readline().split())
# for i in range(N):
#     site, pwd = stdin.readline().split()
#     sitePwd[site] = pwd
# for i in range(M):
#     stdout.write(str(sitePwd[stdin.readline().rstrip()]) + '\n')

# 피보나치 함수 1003번
# from sys import stdin, stdout
# n_list = [[0,0] for _ in range(41)]
# n_list[0], n_list[1] = [1,0], [0,1]
# for i in range(2,41):
#     n_list[i][0] = n_list[i-1][0] + n_list[i-2][0]
#     n_list[i][1] = n_list[i-1][1] + n_list[i-2][1]
# T = int(stdin.readline())
# for i in range(T):
#     index = int(stdin.readline())
#     stdout.write(f'{n_list[index][0]} {n_list[index][1]}\n')

# 1로 만들기 1463번

# from sys import stdin, stdout
# import queue
# N = int(stdin.readline())
# history = [0] * 1000001
# history[N] = 1
# queue = queue.Queue()
# queue.put(N)
# while history[1] == 0:
#     n = queue.get()
#     v1 = n//3
#     v2 = n//2
#     v3 = n-1
#     if n%3 == 0 and history[v1] == 0:
#         queue.put(v1)
#         history[v1] = history[n] + 1
#     if n%2 == 0 and history[v2] == 0:
#         queue.put(v2)
#         history[v2] = history[n] + 1
#     if history[v3] == 0:
#         queue.put(v3)
#         history[v3] = history[n] + 1
# stdout.write(str(history[1] -1) + '\n')

# 계단 오르기 2579번

# from sys import stdin, stdout

# n = int(stdin.readline())

# stairs = [0] * 301
# for i in range(1, n+1):
#     stairs[i] = int(stdin.readline())

# dp = [0] * 301
# dp[1] = stairs[1]
# dp[2] = stairs[1] + stairs[2]
# dp[3] = max(stairs[1]+stairs[3],stairs[2]+stairs[3])

# for i in range(4, n+1):
#     dp[i] = max(dp[i-3] + stairs[i - 1] +  stairs[i], dp[i-2] + stairs[i])

# stdout.write(str(dp[n]) + '\n')

# 바이러스 2606번

# from sys import stdin, stdout

# N = int(stdin.readline())
# P = int(stdin.readline())
# queue = [1] # 연결 정보 확인용 큐 
# check = [0] * 101 # 바이러스에 걸린 컴퓨터 체크
# connect = [[] for _ in range(101)] # 연결 정보 저장 리스트
# for i in range(P):
#     a, b = map(int,stdin.readline().strip().split(' '))
#     connect[a].append(b)
#     connect[b].append(a)
# while len(queue) != 0:
#     computer = queue.pop() # 큐에 저장된 컴퓨터 확인
#     for dest in connect[computer]:
#         if check[dest] == 0:
#             queue.insert(0,dest) # 연결된 컴퓨터 큐에 추가
#             check[dest] = 1 # 바이러스 감염 체크
# if sum(check) == 0:
#     stdout.write('0\n')
# else:
#     stdout.write(str(sum(check) - 1) + '\n')

# 1,2,3 더하기 9095번

# from sys import stdin, stdout

# def factorial(x): # factorial 계산 함수
#     if x == 0 or x == 1:
#         return 1
#     n = 1
#     for i in range(1,x+1):
#         n *= i
#     return n

# def calculate(a,b,c): # 중복이 순열 경우의 수 계산
#     return int(factorial(a+b+c) / (factorial(a) * factorial(b) * factorial(c)))

# def findNumbers(T,hist):
#     s = sum(hist)
#     if s == T:
#         global numbers
#         numbers.append(hist[:])
#         return
#     if s > T:
#         return
#     tmpHist = hist[:]
#     if len(hist) == 0:
#         prev = 3
#     else:
#         prev = hist[-1]
#     for n in range(1,prev+1):
#         tmpHist.append(n)
#         findNumbers(T,tmpHist)
#         del tmpHist[-1]
    
# N = int(stdin.readline())
# numbers = []
# for i in range(N):
#     s = 0
#     T = int(stdin.readline())
#     findNumbers(T,[])
#     for comb in numbers:
#         a,b,c = 0,0,0
#         for n in comb:
#             if n == 3:
#                 a += 1
#             elif n == 2:
#                 b += 1
#             else:
#                 c += 1
#         s += calculate(a,b,c)
#     stdout.write(str(s)+'\n')
#     numbers.clear()

# 패션왕 신해빈 9375

# from sys import stdin, stdout

# T = int(stdin.readline())
# for i in range(T):
#     N = int(stdin.readline())
#     fashion_items = dict()
#     if N == 0:
#         stdout.write('0\n')
#         continue
#     for j in range(N):
#         item, category = stdin.readline().strip().split(' ')
#         if category in fashion_items:
#             fashion_items[category] += 1
#         else:
#             fashion_items[category] = 1
#     if N == 1:
#         stdout.write('1\n')
#         continue
#     s = 1
#     for key in fashion_items.keys():
#         s *= fashion_items[key] + 1
#     stdout.write(str(s-1)+'\n')

# 구간 합 구하기 4 11659번

# from sys import stdin, stdout

# N, M = map(int,stdin.readline().strip().split())
# nums = [0]
# for n in list(map(int,stdin.readline().strip().split())):
#     nums.append(n)
# sums = [0] * (N+1)
# sums[1] = nums[0]
# for i in range(1,N+1):
#     sums[i] = sums[i-1] + nums[i]
# for i in range(M):
#     a,b = map(int,stdin.readline().strip().split())
#     stdout.write(str(sums[b] - sums[a-1])+'\n')

# 2xn 타일링 11726번

# N을 2와 1의 합으로 나타낼 수 있는 경우의 수를 의미

# N = int(input()) # 1 <= N <= 1000
# comb = [0] * 1001
# comb[0], comb[1], comb[2] = 0, 1, 2 # 초깃값 저장
# for i in range(3, N+1):
#     comb[i] = comb[i-1] + comb[i-2]
# print(comb[N] % 10007)

# 2xn 타일링 11727번

# N = int(input()) # 1 <= N <= 1000
# comb = [0] * 1001
# comb[0], comb[1], comb[2] = 0, 1, 3 # 초깃값 저장
# for i in range(3, N+1):
#     comb[i] = comb[i-1] + 2* comb[i-2]
# print(comb[N] % 10007)

# Four Squares 17626번


def solution(N, curList, numList):
    s = sum(curList)
    if s == N:
        return len(curList)
    if s > N:
        return 5
    tmp = numList.copy() # 배열 깊은 복사
    
    

N = int(input())
numList = [] # 1부터 223까지의 제곱을 계산하여 저장한 리스트 223^2 = 49729

for i in range(1,224):
    numList.append(i**2)

tmp = 1
while numList[tmp] <= N: # N보다 작은 숫자들만 리스트에 남김
    tmp += 1
numList = numList[0:tmp]

if N in numList:
    print('1\n')
else:
    for count in range(2,5):
        
