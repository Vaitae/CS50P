def main():
    str=input("Input: ")
    bool=is_valid(str)
    if bool:
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2<=len(s)<=6):
        return False
    if not s.isalnum():
        return False
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    else:
        i=0
        while i<len(s):
            if s[i].isalpha():
                i+=1
            else:
                flag=i
                break
        else:
            return True

        return s[flag]!='0' and s[flag:].isdigit()

if __name__=="__main__":
    main()