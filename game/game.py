import random

def main():
    while True:
        try:
            n=int(input("Level: "))
            if n>0:
                random_num=random.randint(1,n)
                break
            else:
                continue

        except ValueError:
            pass
    while True:
        try:
            guess=int(input("Guess:"))
            if guess==random_num:
                print("Just Right!")
                break
            elif(guess<random_num):
                print("Too small!")
                continue
            else:
                print("Too Large!")
                continue
        except ValueError:
            pass

if __name__=="__main__":
    main()
