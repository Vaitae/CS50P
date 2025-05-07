import re

def main():
    print(count(input("Text: ")))


def count(s):
    um_list=re.findall(r'\b(um)\b', s, re.IGNORECASE)
    return len(um_list)

if __name__ == "__main__":
    main()
