import sys
import csv
from tabulate import tabulate

header=[]
table=[]

if (len(sys.argv))==2:
    read_file=sys.argv[1]

    if (read_file.endswith(".csv")):
        item,ftype=read_file.split(".")
        item=item.title()+" Pizza"
        header=[item,"Small","Large"]

        try:
            with open(read_file) as file:
                reader=csv.DictReader(file)
                for row in reader:
                    table.append([row[item],row["Small"],row["Large"]])
                print(tabulate(table,header,tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a csv file")

elif(len(sys.argv))<2:
    sys.exit("Too few command-line arguments")
else:
    sys.exit("Too many command-line arguments")
