import sys
from PIL import Image,ImageOps

format=(".jpg",".png",".jpeg")
shirt=Image.open("shirt.png")
size=shirt.size

if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
else:
    before=sys.argv[1]
    after=sys.argv[2]
    if (before.endswith(".jpg") and after.endswith(".jpg")) or (before.endswith(".jpeg") and after.endswith(".jpeg")) or (before.endswith(".png") and after.endswith(".png")) :
        try:
            with Image.open(before) as image:
                muppet=ImageOps.fit(image,size)
                muppet.paste(shirt,shirt)
                muppet.save(after)
        except FileNotFoundError:
            sys.exit("Input does not exist")
    elif not before.endswith(format):
        sys.exit("Invalid Input")
    elif not after.endswith(format):
        sys.exit("Invalid Output")
    else:
        sys.exit("Input and output have different extensions.")
