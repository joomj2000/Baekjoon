import sys


N=int(sys.stdin.readline())
target=int(sys.stdin.readline())

dx=[1,0,-1,0]#하우상좌
dy=[0,1,0,-1]
M=N**2
x=y=0
#temp=[]
matrix=[[0]*N for _ in range(N) ]
#print(matrix)
i=0
while(M>0):
    #print(x,y)
    while (N>x>=0 and N>y>=0 and matrix[x][y]==0):
        # if x < 0 or x >= N or y < 0 or y >= N:
        #     continue
        #print(x,y)
        # if matrix[x][y]!=0:
        #     continue
        matrix[x][y]=M
        if M==target:
            target_x=x
            target_y=y
        M-=1
        x += dx[i]
        y += dy[i]
    x-=dx[i]
    y-=dy[i]
    i=(i+1)%4
    x+=dx[i]
    y+=dy[i]

for i in range(N):
    print(*matrix[i])
print(target_x+1,target_y+1)
# def move_snail(x,y):
#     if N>x>0 and N>y>0:
#         for i in range(4):
#             x+=dx[i]
#             y+=dy[i]
#             if x<0 or x>=N or y<0 or y>=N:
#                 continue
#             matrix[x][y]=M
#         # move_snail(x+1,y)
#         # move_snail(x,y+1)
#         # move_snail(x-1,y)
#         # move_snail(x,y-1)
#
#         x+=dx[i]
#         y+=dy[i]
#         matrix[x][y]=M
#         M-=1
#     return
