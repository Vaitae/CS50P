g_list={}

def main():
    while True:
        try:
            item=input()
            if item not in g_list:
                g_list[item]=1
            elif item in g_list:
                g_list[item]+=1

        except EOFError:
            for item in sorted(g_list.keys()):
                print(f"{g_list[item]} {item.upper()}")
            break

main()
