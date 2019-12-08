from collections import Counter

passwordCombinations = []

for value in range(128392, 643281):
    temp = ''
    for i in str(value):
        if len(temp) == 0:
            temp += i
        elif int(i) >= int(temp[-1]):
            temp += i

    if value == int(temp):
        if 2 in Counter(temp).values():
            passwordCombinations.append(temp)

print(len(passwordCombinations))