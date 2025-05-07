def main():
    word=input("Input: ")
    print("Output: ",end="")
    for c in word:
        if c.lower() in ['a','e','i','o','u']:
            continue
        else:
            print(c,end="")
    print()

if __name__=="__main__":
    main()