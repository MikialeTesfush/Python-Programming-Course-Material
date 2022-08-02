word = input("Enter a Word : ")
vow = 0
con = 0
for i in range(len(word )):
    if word [i] in ['a','e','i','o','u']:
        vow = vow + 1
    else:
        con = con + 1
print("Total vowels are:", vow)
print("Total consonants are:", con)