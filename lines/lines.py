import sys

if(len(sys.argv)==2):
    pyfile=sys.argv[1]
    if pyfile.endswith(".py"):
        try:
            with open(pyfile) as file:
                count=0
                for line in file:
                    if line.lstrip().startswith("#"):
                        continue
                    elif line.isspace():
                        continue
                    count+=1
                print(count)

        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a Python file")

elif(len(sys.argv)>2):
    sys.exit("Too many command-line arguments")

else:
    sys.exit("Too few command-line arguments")
