str=input("Input: ")

print("Output: ",end=" ")
#print(str)

for c in str:
    if c.isupper():
        print("_"+c.lower(),end="")
    else:
        print(c,end="")
print()
