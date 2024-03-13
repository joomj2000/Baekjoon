from collections import deque

N, K = map(int, input().split(' '))
people_list = deque()
people_list.extend(i for i in range(1, N + 1))
result = []
index = 1
while len(people_list) > 0:
    if index % K == 0:
        result.append(people_list.popleft())
    else:
        people_list.append(people_list.popleft())
    index += 1

print("<", end='')
for i in result[:-1]:
    print(i, end=', ')
print(result[-1], end=">")
