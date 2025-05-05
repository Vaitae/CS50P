greet=input("Greeting: ")
greet=greet.strip()
if((greet=="hello") or (greet=="Hello") or ("hello" in greet) or ("Hello" in greet)):
    print("$0")
elif(greet.startswith("h") or greet.startswith("H")):
    print("$20")
else:
    print("$100")
