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