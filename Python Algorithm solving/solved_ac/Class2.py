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

# 균형잡힌 세상 4949번

# def check(words):
#     stack = [0 for _ in range(100)]
#     tos = -1
#     for w in words:
#         if w == '(' or w == '[':
#             tos += 1
#             stack[tos] = w
#         elif w == ')' or w == ']':
#             if tos == -1:
#                 return False
#             if w == ')' and stack[tos] != '(':
#                 return False
#             elif w == ']' and stack[tos] != '[':
#                 return False
#             tos -= 1
#     if tos != -1 :
#         return False
#     return True

# from sys import stdin, stdout
# words = stdin.readline().rstrip()
# while words != '.':
#     if check(words):
#         stdout.write('yes\n')
#     else:
#         stdout.write('no\n')
#     words = stdin.readline().rstrip()

# 제로 10773번

# from sys import stdin, stdout
# N = int(stdin.readline())
# n_list = []
# for i in range(N):
#     n = int(stdin.readline())
#     if n == 0:
#         del n_list[-1]
#     else:
#         n_list.append(n)
# stdout.write(str(sum(n_list)) + '\n')

# solved.ac 18110번

# from sys import stdin, stdout
# N = int(stdin.readline())
# if N == 0:
#     stdout.write('0\n')
# else:
#     dif = [0 for _ in range(30)]
#     for i in range(N):
#         dif[int(stdin.readline())-1] += 1
#     cutN = round(N*0.15 + 1e-9)
#     i = 0
#     count = 0
#     while count != cutN:
#         if dif[i] > 0:
#             dif[i] -= 1
#             count += 1
#         else:
#             i += 1

#     i = 29
#     count = 0
#     while count != cutN:
#         if dif[i] > 0:
#             dif[i] -= 1
#             count += 1
#         else:
#             i -= 1

#     S = 0
#     for i in range(30):
#         S += dif[i] * (i+1)
#     avg = round(S/sum(dif) + 1e-9)
#     stdout.write(str(avg) + '\n')

# 소수 구하기 1929번

# from sys import stdin, stdout
# M, N = map(int,stdin.readline().split())
# n_list = [1 for _ in range(N)]
# n_list[0] = 0
# for i in range(1,N-1):
#     if n_list[i] != 0:
#         n = i + 1
#         for j in range(i+n,N,n):
#             n_list[j] = 0
# for i in range(M-1,N):
#     if n_list[i] == 1:
#         stdout.write(str(i+1) + '\n')

# 프린터 큐 1966번
from sys import stdin, stdout
testCase = int(input())
for i in range(testCase):
    N, M = map(int, stdin.readline().split())
    n_list = list(map(int,stdin.readline().split()))
    count = 1
    while 1:
        if n_list[0] >= max(n_list):
            if M == 0:
                stdout.write(f'{count}\n')
                break
            else:
                del n_list[0]
                M -= 1
                count += 1
        else:
            if M == 0:
                M = len(n_list)-1
                n_list.append(n_list[0])
                del n_list[0]
            else:
                n_list.append(n_list[0])
                del n_list[0]
                M -= 1