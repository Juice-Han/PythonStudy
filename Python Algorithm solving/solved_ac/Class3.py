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