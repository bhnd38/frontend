groceries={}

while True:


    try:
        grocery=input().upper()
        if grocery not in groceries:
            groceries[grocery]=1


        elif grocery in groceries:
            groceries[grocery]+=1



    except EOFError:
        print()
        for key, val in sorted(groceries.items()):
            print(f"{val} {key}")

        break

