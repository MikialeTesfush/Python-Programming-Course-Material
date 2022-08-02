num = int(input("Enter number: "))
reverse = 0
while(num!= 0):
    rem = num % 10
    reverse = (reverse * 10) + rem
    num = num//10
print("the reverse of the number is: ",reverse)