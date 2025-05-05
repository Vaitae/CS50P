def main():
    time=input("What time is it? ")
    ntime=time.strip("a.m.").strip("p.m.")
    ctime=convert(ntime)
    if(ctime>=7 and ctime<=8):
        print("breakfast time")
    elif(ctime>=12 and ctime<=13):
        print("lunch time")
    elif(ctime>=18 and ctime<=19):
        print("dinner time")

def convert(time):
    x, y= time.split(":")
    x=float(x)
    y=float(y)/60
    ntime=x+y
    return ntime

if __name__ == "__main__":
    main()
