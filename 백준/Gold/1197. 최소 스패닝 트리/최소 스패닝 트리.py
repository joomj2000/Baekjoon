import sys
def find_set(x): #연결된 최고 조상 확인
    if p[x] != x:
        p[x] = find_set(p[x]) # path compression
    return p[x]

def union(x, y): #차수가 더 작은 트리가 차수가 더 큰 트리 밑으로 들어감
    if r[x] > r[y]:
        p[y] = x
    else:
        p[x] = y
        if r[x] == r[y]:
            r[y] += 1


V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: (x[2])) # 가중치 기준으로 정렬
p = list(range(V+1))
r = [0] * (V+1) #차수를 저장할 배열
answer = 0
cnt = 0

for s, e, w in edges:
    if find_set(s) != find_set(e): #사이클이 아닐때
        union(find_set(s), find_set(e)) #합치기
        answer += w
        cnt += 1
        if cnt == V:
            break

print(answer)