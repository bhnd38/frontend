import inflect
p= inflect.engine()


# def listup(a):
#     if len(a) >= 2:
#         print(f"Adieu, adieu, to {', '.join(a[0:-1])} and {a[-1]}")
#     elif len(a)==1:
#         print(f"Adieu, adieu, to {a[0]}")

names=[]
while True:

    try:

        name = input("Name: ")
        names.append(name)


    except EOFError:
        # listup(names)
        print()
        print(f"Adieu, adieu, to {p.join(names)}")
        break
