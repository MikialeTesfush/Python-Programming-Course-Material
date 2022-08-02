count = 0
for i in range(200):
    if i%7 == 0:
        print(i,end=" ")
        count = count+1
        if count == 8:
            break