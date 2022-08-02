word = input("Enter a Word :")
x = []
for i in range(len(word)):
    if word[i] not in x:
        x.append(word[i])
    else:
        pass
for i in range(len(x)):
    print(x[i], end=" ")