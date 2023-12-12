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

# 덱 10866번

# from sys import stdin, stdout
# N = int(input())
# deque = [0 for _ in range(10000)]
# f = 0
# b = 1
# def push_front(deque,v):
#     global f
#     deque[f] = v
#     f = (f + 9999) % 10000
# def push_back(deque,v):
#     global b
#     deque[b] = v
#     b = (b + 10001) % 10000
# def pop_front(deque):
#     global f,b
#     if (f + 10001) % 10000 == b:
#         stdout.write('-1\n')
#     else:
#         f = (f + 10001) % 10000
#         stdout.write(str(deque[f]) + '\n')
# def pop_back(deque):
#     global f,b
#     if (f + 10001) % 10000 == b:
#         stdout.write('-1\n')
#     else:
#         b = (b + 9999) % 10000
#         stdout.write(str(deque[b]) + '\n')
# def size():
#     global f,b
#     s = (b-f+9999)%10000
#     stdout.write(str(s)+'\n')
# def empty():
#     global f,b
#     if (f + 10001) % 10000 == b:
#         stdout.write('1\n')
#     else:
#         stdout.write('0\n')
# def front(deque):
#     global f,b
#     if (f + 10001) % 10000 == b:
#         stdout.write('-1\n')
#     else:
#         stdout.write(str(deque[(f+10001)%10000])+'\n')
# def back(deque):
#     global f,b
#     if (f + 10001) % 10000 == b:
#         stdout.write('-1\n')
#     else:
#         stdout.write(str(deque[(b+9999)%10000])+'\n')

# for i in range(N):
#     op = stdin.readline().strip()
#     if 'push_front' in op:
#         op, v = op.split()
#         push_front(deque,int(v))
#     elif 'push_back' in op:
#         op, v = op.split()
#         push_back(deque,int(v))
#     elif op == 'pop_front':
#         pop_front(deque)
#     elif op == 'pop_back':
#         pop_back(deque)
#     elif op == 'size':
#         size()
#     elif op == 'empty':
#         empty()
#     elif op == 'front':
#         front(deque)
#     else:
#         back(deque)

# 덩치 7568번

# from sys import stdin, stdout
# N = int(stdin.readline().strip())
# people = []
# for i in range(N):
#     people.append(list(map(int,stdin.readline().split())))

# grade = [1 for _ in range(N)]
# for i in range(N-1):
#     for j in range(i+1,N):
#         if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
#             grade[j] += 1
#         elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:
#             grade[i] += 1
# for g in grade:
#     stdout.write(str(g) + ' ')

# 좌표 정렬하기 2 11651번

# from sys import stdin, stdout
# N = int(stdin.readline())
# y_list = [[] for _ in range(200001)]
# for i in range(N):
#     x, y = map(int,stdin.readline().split())
#     y_list[y+100000].append(x)
# for i in range(200001):
#     y_list[i].sort()
#     if len(y_list[i]) != 0:
#         for x in y_list[i]:
#             stdout.write(f'{x} {i-100000}\n')

# 설탕 배달 2839번
# N = int(input())
# count = -1
# f = N // 5
# while f >= 0 :
#     if (N-5*f) % 3 == 0:
#         t = (N-5*f) // 3
#         count = f + t
#         break
#     f -= 1
# print(count)