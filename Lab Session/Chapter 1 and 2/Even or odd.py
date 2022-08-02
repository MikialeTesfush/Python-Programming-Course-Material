x = [10,23,24,35,65,78,90]
eve = []
odd = []
for i in range(len(x)):
    if x[i] % 2 == 0:
        eve.append(x[i])
    else:
        odd.append(x[i])
print("Even numbers are: ",eve)
print("Odd numbers are: ",odd)