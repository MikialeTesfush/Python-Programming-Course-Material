c=0
d=0
x=int(input("enter no1 :"))
y=int(input("enter no2 :"))
for x in range(x,y):
    if(x%2==0):
        c=c+1
    elif x%2!=0:
        d=d+1
print("even :",c)
print("odd :",d)