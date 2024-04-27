import sys
from collections import deque
import copy
sys.setrecursionlimit(100000000)

def DFS(x,y,color):
    if x<=-1 or x>=6 or y<=-1 or y>=12:
        return False
    if Graph2[x][y]==color:
        #color=Graph2[x][y]
        global result
        result+=1
        Graph2[x][y]='.'
        DFS(x-1,y,color)
        DFS(x,y-1,color)
        DFS(x+1,y,color)
        DFS(x,y+1,color)
        return True
    return False


    #while(queue):

def boom():
    global Graph2
    GG=[]
    for i in range(6):
        GGG=deque([])
        for j in range(12):
            if Graph2[i][j]=='.':
                continue
            else:
                GGG.append(Graph2[i][j])
        for k in range(12-len(GGG)):
            GGG.appendleft('.')
        GG.append(GGG)
    Graph2=GG
    #print(Graph2)


    # cnt = 0
    # while cnt < 12:
    #     if Graph2[i][-1] == '.':
    #         Graph2[i].pop()
    #         Graph2[i].appendleft('.')
    #     cnt += 1




#탐색하면서 방문시 .로 바꿈
#연결요소의 개수가 4이하이면 이전에 복사해논 걸 사용
#연결요소의 개수가 4이상이면 .으로 바꾼걸 놔두고 .으로 바뀐 것들의 위를 탐색하여 아래로 내려야함
result=0
Graph=[]
is_boom=False
for _ in range(12):
    temp=list(sys.stdin.readline().strip())
    Graph.append(temp)
Graph2=[deque(t) for t in zip(*Graph)]
#print(Graph2)
queue=[]
#print(Graph2[5][-1])
answer=0
while(True):
    for i in range(6):
        for j in range(12):
            temp_Graph= copy.deepcopy(Graph2)
            if Graph2[i][j]!='.' and DFS(i,j, Graph2[i][j])==True : #처음 방문
                #print(Graph2[i][j])
                if result>=4:
                    is_boom=True
                   # print("터뜨리기",Graph2[i][j])
                    #터뜨리기

                else:
                    Graph2=temp_Graph
                result=0
        #print(is_boom)
    if is_boom==False:
        break
    #boom()
    answer+=1
    boom()
    #print(Graph2)
    is_boom=False

#print(Graph2)
print(answer)


