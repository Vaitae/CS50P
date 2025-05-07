def main():
    str=input("Input: ")
    print(shorten(str))

def shorten(str):
    print("Output: ",end="")
    words=""
    for c in str:
        if c.lower() in ['a','i','e','o','u']:
            continue
        else:
            words+=c
    return words

if __name__=="__main__":
    main()
