import sys


def DFS(x,y):
    #visited[V] = 0
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    if Graph[x][y]==1:
        global result
        result+=1
        Graph[x][y]=0
        DFS(x-1,y)
        DFS(x,y-1)
        DFS(x+1,y)
        DFS(x,y+1)
        return True
    return False


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    Graph=[]
    total_result=0
    num_list=[]
    result=0
    for _ in range(n):
        Graph.append(list(map(int,sys.stdin.readline().strip())))
    for i in range(n):
        for j in range(n):
            if DFS(i,j)==True:
                total_result+=1
                num_list.append(result)
                result = 0

    print(total_result)
    num_list.sort()
    for i in num_list:
        print(i)
