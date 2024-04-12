o=50


while o<=50:
    q=int(input(f"\nAmount Due: {o}\nInsert Coin: "))

    if q==25 or q==10 or q==5:
        o=o-q
    else:
        o=o
    if o==0:
        print("\nChange Owed: 0")
        break
    elif o<0:
        print(f"\nChange Owed: {o*-1}")
        break
