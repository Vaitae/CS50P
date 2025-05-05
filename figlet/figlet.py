
from pyfiglet import Figlet
import sys
import random

f = Figlet()
font_list = f.getFonts()

def main():
    try:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font" :
            for font in font_list :
                if sys.argv[2] == font:
                    user_font = font

                if sys.argv[2] not in font_list :
                    sys.exit("Invalid usage")
        else :
            sys.exit("Invalid usage")
    except IndexError : pass

    if len(sys.argv) == 2:
        sys.exit("Invalid usage")

    if len(sys.argv) == 1:
        user_font = font_list[random.randint(0,10)]

    f.setFont(font=user_font)

    userinput = input("Input: ")

    print (f.renderText(userinput))

if __name__=="__main__":
    main()
