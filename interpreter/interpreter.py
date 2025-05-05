exp=input("Expression: ")
x, y, z=exp.split(" ")
x=int(x)
z=int(z)
if(y=="+"):
    print(float(x+z))
elif(y=="-"):
    print(float(x-z))
elif(y=="*"):
    print(float(x*z))
elif(y=="/")and(z!=0):
    print(float(x/z))