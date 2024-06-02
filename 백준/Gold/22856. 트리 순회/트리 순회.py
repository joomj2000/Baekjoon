import sys
sys.setrecursionlimit(1000000)


N=int(sys.stdin.readline())



Right=[[] for _ in range(N+1)]
Left=[[] for _ in range(N+1)]
visited=[1]
visited_in=[1]
for _ in range(N):
    v1,v2,v3=map(int,sys.stdin.readline().split())
    if v2!=-1:
        Left[v1].append(v2)
    if v3!=-1:
        Right[v1].append(v3)

def inorder(n):
    left = right = -1
    for left in Left[n]:
        if left not in visited_in:
            inorder(left)
            # print(n)
            #cnt += 1

    visited_in.append(n)

    for right in Right[n]:
        if right not in visited_in:
            #visited_in.append(right)
            inorder(right)
            # print(n)
            #cnt += 1


def order(n):
    #print(visited,N,n)
    global cnt
    cnt+=1

    left=right=-1
    for left in Left[n]:
        # if left not in visited:
        visited.append(left)
        order(left)
        #print(n)
        cnt+=1

    #print(visited)
    if visited_in[-1]==n:
        print(cnt)
        exit(0)

    for right in Right[n]:
        #if right not in visited:
        visited.append(right)
        order(right)
        #print(n)
        cnt+=1

cnt=-1
#visited.append(1)
inorder(1)
#print(visited_in)
order(1)
#print(cnt)