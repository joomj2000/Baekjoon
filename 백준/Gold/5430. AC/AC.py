import sys
from collections import deque
N = int(sys.stdin.readline())
deque = deque([])

def action(command):
    cnt=0
    for i in command:
        if i == 'R':
            cnt += 1
        elif i == 'D':
            if len(deque) == 0:
                print('error')
                return
            if cnt % 2 == 0:
                deque.popleft()
            else:
                deque.pop()

    print('[', end='')
    while len(deque) > 1:
        if cnt % 2 == 0:
            print(deque.popleft(), end=',')
        else:
            print(deque.pop(), end=',')
    if (len(deque) == 1):
        print(deque.pop(), end='')
    print(']')


for _ in range(N):
    command = sys.stdin.readline()
    n = int(sys.stdin.readline())
    number = sys.stdin.readline()
    number = number.replace('[', '').replace(']', '').replace('\n', '')
    if n != 0:
        number_list = [int(x) for x in number.split(',')]
        for j in number_list:
            deque.append(int(j))

    action(command)