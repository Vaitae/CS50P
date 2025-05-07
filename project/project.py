from tabulate import tabulate
import sys

database=[]

def main():
    print("----------------To-Do List----------------")
    instructions=[
        ["Press A","To Add a Task"],
        ["Press D","To Delete a Task"],
        ["Press M","To Mark a Task as Done"],
        ["Press V","To View the List"],
        ["Press S","To Save the list"],
        ["Press E","To Exit"]]
    task_head=["Options","Action"]
    print(tabulate(instructions, task_head, tablefmt="rounded_outline"))

    while True:
        user_input=input("Enter the action: ")
        if user_input.lower()=="a":
            task=input("Enter the task: ")
            add(task)
        elif user_input.lower()=="d":
            display()
            try:
                option = int(input("Enter the task no. you want to delete: "))
                delete(option)
            except ValueError:
                print("Please enter a valid number! ◉_◉")
        elif user_input.lower()=="m":
            display()
            try:
                number=int(input("Enter the task number to mark as done: "))
                if 0 < number <= len(database):
                    database[number-1]["status"]="done"
                    print("Marked as done! (˶˃ ᵕ ˂˶)")
                else:
                    print("Invalid task number (¬_¬”)")
            except ValueError:
                print("Please enter a valid number ◉_◉")

        elif user_input.lower()=="v":
            display()
        elif user_input.lower()=="s":
            save()
        elif user_input.lower()=="e":
            sys.exit("Thanks for using this app! („• ֊ •„)")
        else:
            break

def add(task):
    database.append({"task":task.capitalize(),"status":"pending"})
    print("Added Successfully! (˶ᵔ ᵕ ᵔ˶)")

def delete(i):
    n=len(database)
    if i<=n and i>0:
        for num in range(len(database)):
            if num==(i-1):
                removed=database.pop(i-1)
                print(f"Deleted {removed['task']} Successfully! (˶ᵔ ᵕ ᵔ˶)")
            else:
                continue
    else:
        print("Try Again! (¬_¬”)")


def display():
    print("--------------------------------")
    if database:
        for i, item in enumerate(database, start=1):
            status_icon = "✅" if item["status"] == "done" else "⬜"
            print(f"{i}. {status_icon} {item['task']}")
            print("--------------------------------")
    else:
        print("Empty List! (¬_¬”)")
        print("--------------------------------")

def save():
    with open("todo-list.txt", "w") as file:
        for i, item in enumerate(database, start=1):
            file.write(f"{i}. {item['task']} [{item['status'].upper()}]\n")
    print("Saved (˶˃ ᵕ ˂˶)")

if __name__ == "__main__":
    main()
