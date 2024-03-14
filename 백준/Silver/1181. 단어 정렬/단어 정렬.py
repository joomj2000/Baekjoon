N = int(input())
word_set={input() for _ in range(N)}
word_list=list(word_set)
word_list.sort()
word_list.sort(key=len)
for word in word_list:
    print(word)
