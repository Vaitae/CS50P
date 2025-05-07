def main():
    str=input("Fraction: ")
    frac=convert(str)
    print(gauge(frac))

def convert(fraction):
    while True:
        try:
            x, y=fraction.split("/")
            p=int(x)
            q=int(y)
            if q==0:
                raise ZeroDivisionError
            elif p>q:
                raise ValueError
            else:
                result=round((p/q),2)
                return int(result*100)
        except (ValueError, ZeroDivisionError):
                raise

def gauge(p):
    if(p<=1):
        return "E"
    elif p>=99:
        return "F"
    else:
        return f"{p}%"

if __name__ == "__main__":
    main()
