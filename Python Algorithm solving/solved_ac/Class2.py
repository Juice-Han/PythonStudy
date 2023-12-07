# 수 찾기 1920번
# import sys
# N = int(input())
# n_dict = dict.fromkeys(map(int,sys.stdin.readline().strip().split()))
# M = int(input())
# m_list = list(map(int,sys.stdin.readline().strip().split()))
# for m in m_list:
#     if m in n_dict:
#         sys.stdout.write('1\n')
#     else:
#         sys.stdout.write('0\n')

# 카드2 2164번

# N = int(input())
# n_list = [i+1 for i in range(N)]
# while len(n_list) != 1:
#     tmp = n_list[1::2]
#     if len(n_list) % 2 != 0:
#        tmp.insert(0,n_list[-1])
#     n_list = tmp
# print(n_list[0])

# 괄호 9012번
# class MyStack:
#     def __init__(self,size):
#         self.size = size
#         self.p = -1
#         self.stack = [0 for _ in range(size)]
    
#     def push(self,v):
#         self.p += 1
#         self.stack[self.p] = v
    
#     def pop(self):
#         if self.p == -1:
#             return -1
#         tmp = self.stack[self.p]
#         self.p -= 1
#         return tmp

#     def __str__(self):
#         return str(self.stack)

# N = int(input())
# for i in range(N):
#     stack = MyStack(50)
#     ex = input()
#     b = True
#     for p in ex:
#         if p == '(':
#             stack.push(p)
#         else:
#             if stack.pop() != '(':
#                 b = False
#                 break
#     if stack.pop() != -1:
#         b = False
#     if b:
#         print('YES')
#     else:
#         print('NO')

# 숫자 카드 2 10816번
# import sys
# N = int(input())
# n_list = list(map(int,sys.stdin.readline().strip().split()))
# n_dict = dict()
# for n in n_list:
#     if n in n_dict:
#         n_dict[n] += 1
#     else:
#         n_dict[n] = 1

# M = int(input())
# m_list = list(map(int,sys.stdin.readline().strip().split()))
# for m in m_list:
#     if m in n_dict:
#         sys.stdout.write(str(n_dict[m]) + ' ')
#     else:
#         sys.stdout.write('0 ')

# 스택 10828번
# import sys
# N = int(input())
# print = sys.stdout.write
# stack = []
# for i in range(N):
#     op = sys.stdin.readline().strip()
#     if 'push' in op:
#         _, v = op.split()
#         stack.append(int(v))
#     elif op == 'pop':
#         if len(stack) == 0:
#             print('-1\n')
#         else:
#             print(str(stack[-1])+'\n')
#             del stack[-1]
#     elif op == 'size':
#         print(str(len(stack))+'\n')
#     elif op == 'empty':
#         if len(stack) == 0:
#             print('1\n')
#         else:
#             print('0\n')
#     else:
#         if len(stack) == 0:
#             print('-1\n')
#         else:
#             print(str(stack[-1])+'\n')

# 큐 10845번

# import sys
# input = sys.stdin.readline
# print = sys.stdout.write
# queue = []
# front = -1
# back = -1
# N = int(input().strip())
# for i in range(N):
#     op = input().strip()
#     if 'push' in op:
#         op, v = op.split()
#         queue.append(int(v))
#         back += 1
#     elif op == 'pop':
#         if front == back:
#             print('-1\n')
#         else:
#             front += 1
#             print(str(queue[front]) + '\n')
#     elif op == 'size':
#         print(str(back - front) + '\n')
#     elif op == 'empty':
#         print('1\n') if front == back else print('0\n')
#     else:
#         if front == back:
#             print('-1\n')
#         elif op == 'front':
#             print(str(queue[front+1]) + '\n')
#         else:
#             print(str(queue[back]) + '\n')
