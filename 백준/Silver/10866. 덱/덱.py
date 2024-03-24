import sys
from collections import deque
deque=deque([])
N = int(sys.stdin.readline())

for _ in range(N):
    command=sys.stdin.readline()
    if 'push_front' in command:
        num=int(command.split(' ')[1])
        deque.appendleft(num)
    elif 'push_back' in command:
        num=int(command.split(' ')[1])
        deque.append(num)
    elif 'pop_front' in command:
        if len(deque)==0:
            print(-1)
        else:
            print(deque.popleft())
    elif 'pop_back' in command:
        if len(deque)==0:
            print(-1)
        else:
            print(deque.pop())
    elif 'size' in command:
        print(len(deque))
    elif 'empty' in command:
        print(0 if len(deque) > 0 else 1)
    elif 'front' in command:
        if len(deque)==0:
            print(-1)
        else:
            print(deque[0])
    elif 'back' in command:
        if len(deque)==0:
            print(-1)
        else:
            print(deque[-1])
