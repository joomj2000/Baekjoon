N = int(input())
people_list = []

for _ in range(N):
    temp = input()
    age = int(temp.split(' ')[0])
    name = temp.split(' ')[1]
    people_list.append((age, name))

people_list.sort(key = lambda x : x[0])

for i in people_list:
    print(i[0], i[1])
