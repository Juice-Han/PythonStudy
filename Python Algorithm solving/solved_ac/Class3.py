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

from sys import stdin, stdout

n = int(stdin.readline())

stairs = [0] * 301
for i in range(1, n+1):
    stairs[i] = int(stdin.readline())

dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1]+stairs[3],stairs[2]+stairs[3])

for i in range(4, n+1):
    dp[i] = max(dp[i-3] + stairs[i - 1] +  stairs[i], dp[i-2] + stairs[i])

stdout.write(str(dp[n]) + '\n')