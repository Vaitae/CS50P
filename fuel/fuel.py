def main():
    while True:
        try:
            number=input("Fraction: ")
            x, y=number.split("/")
            p=int(x)
            q=int(y)
            result=round((p/q),2)

            if 1>=result>=0.99:
                print("F")
            elif result<=0.01:
                print("E")
            elif p>q :
                continue
            else:
                print(f"{int(result*100)}%")

        except (ValueError, ZeroDivisionError):
            pass
        else:
             break

main()
