import requests
import json
import sys

def main():
    if(len(sys.argv)==2):
        try:
            bitcoin=float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
    elif(len(sys.argv)==1):
        sys.exit("Missing command-line argument")
    else:
        sys.exit()
#print(bitcoin)
    try:
        response=requests.get("https://api.coincap.io/v2/assets/bitcoin")
        #print(response)
        response.raise_for_status()
    except requests.RequestException:
        print("Couldn't connect!")

    #content=json.dumps(response.json(),indent=2)
    #print(content)
    o=response.json()
    for key, value in o["data"].items():
        if key=="priceUsd":
            cost_for_one=float(value)
        else:
            continue

    amount=cost_for_one*bitcoin
    print(f"${amount:,.4f}")

if __name__=="__main__":
    main()
