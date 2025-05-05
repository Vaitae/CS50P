def main():
    change=50
    while change!=0:
        print("Amount Due:",change)
        coin=int(input("Insert Coin: "))
        if(coin==25 or coin==5 or coin==10):
            change=change-coin
        if change<=0:
            print("Change Owed:",-change)
            break

main()
