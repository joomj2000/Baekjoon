def excursion(str):
    digits = [0, 0, 0]
    x = 0
    for i in range(len(str)):
        for j in range((int(str[i])) + 1, 3):
            x += digits[j]
        digits[int(str[i])] += 1
    return x

print(excursion(input()))