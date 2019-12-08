passwordCombinations = []

for value in range(128392, 643281):
    temp = ''
    for i in str(value):
        if len(temp) == 0:
            temp += i
        elif int(i) >= int(temp[-1]):
            temp += i

    if value == int(temp):
        if len(set(temp)) != len(temp):
            passwordCombinations.append(temp)

print(len(passwordCombinations))