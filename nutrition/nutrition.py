fruits_dict={
    "Apple":"130",
    "Avocado":"50",
    "Banana":"110",
    "Cantaloupe":"50",
    "Grapefruit":"60",
    "Grapes":"90",
    "Honeydew Melon":"50",
    "Kiwifruit":"90",
    "Lemon":"15",
    "Lime":"20",
    "Nectarine":"60",
    "Orange":"80",
    "Peach":"60",
    "Pear":"100",
    "Pineapple":"50",
    "Plum":"70",
    "Strawberries":"50",
    "Sweet Cherries":"100",
    "Tangerine":"50",
    "Watermelon":"80"
}

def main():
    fruit=input("Item: ").lower().title()
    for fru in fruits_dict:
        if fru==fruit:
           print(f"Calories: {fruits_dict[fru]}")

main()