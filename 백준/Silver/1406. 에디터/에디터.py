import sys

'''
append(): O(1)
pop(): O(1)
insert(): O(N)
'''

front_cursor=list(sys.stdin.readline().strip())
back_cursor=[]

N=int(sys.stdin.readline())
for _ in range(N):
    command=sys.stdin.readline().strip()
    if 'P' in command:
        new=command.split(' ')[1]
        front_cursor.append(new)

    elif 'L' in command:
        if len(front_cursor)!=0:
            back_cursor.append(front_cursor.pop())
    elif 'D' in command :
        if len(back_cursor) != 0:
            front_cursor.append(back_cursor.pop())
    elif 'B'  in command :
        if len(front_cursor) != 0:
            front_cursor.pop()
print(*front_cursor, sep='',end='')
back_cursor.reverse()
print(*back_cursor, sep='')
