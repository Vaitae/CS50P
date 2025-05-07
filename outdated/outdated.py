month_list = [
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
]

def main():
    while True:
        try:
            date = input("Date: ")

            #Input type 1
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

                if 1 <= day <= 31 and 1 <= month <= 12:
                    print(f"{year}-{month:02}-{day:02}")
                    break
            
            #Input type 2
            elif "," in date:
                m, d, y = date.split(" ")
                month_str = m
                day = int(d.strip(","))
                year = int(y)

                if month_str in month_list:
                    month = month_list.index(month_str) + 1

                    if 1 <= day <= 31 and 1 <= month <= 12:
                        print(f"{year}-{month:02}-{day:02}")
                        break

        except ValueError:
            pass

main()
