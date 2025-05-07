def main():
    str=input("Input: ")
    if isvalid(str):
        print("Valid")
    else:
        print("Invalid")

def isvalid(s):
    #“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if len(s)>6 or len(s)<2:
        return False

    #"All vanity plates must start with at least two letters.”
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    #“Numbers cannot be used in the middle of a plate; they must come at the end.
    # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    # The first number used cannot be a ‘0’.”
    if s.isalnum():
        num_list=[]
        if s[0]=='0':
            return False
        for c in s:
            if c.isalpha():
                continue
            else:
                num=int(c)
                num_list.append(num)
            if num_list[0]==0:
                return False
            if s[num:].isalnum() and s[:-num].isalpha():
                return False

    #“No periods, spaces, or punctuation marks are allowed.”
    for c in s:
        if c in [","," ",".","?"]:
            return False
    return True

main()
