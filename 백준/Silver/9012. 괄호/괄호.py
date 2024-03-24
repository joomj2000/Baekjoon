import sys
N = int(sys.stdin.readline())
for _ in range(N):
    stack=[]
    PS = sys.stdin.readline().split('\n')[0]
    for i in PS:
        if i=='(':
            stack.append(i)
        else:
            if len(stack)==0:
                stack.append(i)
                break
            stack.pop()
    if len(stack)!=0:
        print("NO")
    else:
        print("YES")