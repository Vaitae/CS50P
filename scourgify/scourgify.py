import sys
import csv

after=[]

if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        bfrfile=sys.argv[1]
        aftfile=sys.argv[2]
        try:
            with open(bfrfile) as in_file:
                reader=csv.DictReader(in_file)
                for row in reader:
                    lname,fname=row["name"].split(",")
                    after.append({'first':fname.lstrip(),'last':lname,'house':row["house"]})
        except FileNotFoundError:
            sys.exit(f"Could not read {bfrfile}")

        with open(aftfile,"w") as out_file:
            writer=csv.DictWriter(out_file,fieldnames=["first","last","house"])
            writer.writeheader()
            for i in after:
                writer.writerow({"first":i["first"],"last":i["last"],"house":i["house"]})
    else:
        sys.exit("Not a csv file")
