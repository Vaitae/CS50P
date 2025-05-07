import random

def main():
    level=get_level()
    print(level)
    score=0
    for _ in range(10):
        trial=0
        x=generate_integer(level)
        y=generate_integer(level)
        #print(x,y)
        while(trial<3):
            print(f" {x} + {y} = ",end="")
            sum=x+y
            try:
                guess=int(input())
                if guess==sum:
                    score+=1
                    break

                else:
                    print("EEE")
                    trial+=1
                    continue
            except ValueError:
                print("EEE")
                trial+=1
                continue
        if(trial==3):
            print(f"{x} + {y} = {sum}")
    print("Score:",score)



def get_level():
    while True:
        try:
            level=int(input("Level: "))
            if(level==1 or level==2 or level==3):
                return level
            elif(level!=1 or level!=2 or level!=3):
                continue
            else:
                raise ValueError()
        except ValueError:
            continue

def generate_integer(level):
    if(level==1):
        x=random.randint(0,9)
    elif(level==2):
        x=random.randint(10,99)
    else:
        x=random.randint(100,999)
    return x

if __name__ == "__main__":
    main()
