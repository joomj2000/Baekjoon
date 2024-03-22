import sys
N = int(sys.stdin.readline())
stack =[]
for _ in range(N):
    command=sys.stdin.readline()
    #print(command)
    if 'push' in command:
        num=int(command.split(' ')[1])
        stack.append(num)
    elif 'pop' in command:
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif 'size' in command:
        print(len(stack))
    elif 'empty' in command:
        print(0 if len(stack) > 0 else 1)
    elif 'top' in command:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])