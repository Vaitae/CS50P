from emoji import emojize

def main():
    text_to_emo=input("Input: ")
    print(f"Output: {emojize(text_to_emo, language='alias')}")

if __name__=="__main__":
    main()
