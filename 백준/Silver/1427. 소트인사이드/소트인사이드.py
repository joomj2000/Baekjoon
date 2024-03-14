N = input()
num_list=[]
for i in N:
    num_list.append(int(i))
num_list.sort(reverse=True)
print(str(num_list).replace(', ','').replace('[','').replace(']',''))