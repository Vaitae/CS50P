import inflect

p=inflect.engine()
name_list=[]

def main():
    try:
        while True:
            name=input("Name: ").capitalize()
            name_list.append(name)
    except EOFError:
        print("Adieu, adieu, to ",end="")
        print(p.join(name_list))

if __name__=="__main__":
    main()
