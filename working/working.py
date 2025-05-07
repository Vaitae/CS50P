import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    isRightFormat = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$",s)
    if isRightFormat:
        pieces = isRightFormat.groups()
        if int(pieces[1])>12 or int(pieces[5])>12:
            raise ValueError
        first_time=new_format(pieces[1], pieces[2], pieces[3])
        second_time=new_format(pieces[5], pieces[6], pieces[7])
        return f"{first_time} to {second_time}"
    else:
        raise ValueError

def new_format(hour, minute, ampm):
    if ampm=="PM":
        if int(hour)==12:
            new_hr=12
        else:
            new_hr=int(hour)+12
    else:
        if int(hour)==12:
            new_hr=0
        else:
            new_hr=int(hour)
    if minute == None:
        new_min=':00'
        new_time=f"{new_hr:02}"+new_min
    else:
        new_time=f"{new_hr:02}"+":"+minute
    return new_time

if __name__ == "__main__":
    main()
