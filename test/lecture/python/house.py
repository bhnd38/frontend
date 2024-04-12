name = input("What's your name? ")
'''
if name == "Harry" or "Hermaione" or 'Ron':
    print("Gryffindor")
elif name == "Drako":
    print('Slytherin')
else:
    print("Who")

'''

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermaione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print('Slytherin')
    case _:
        print('Who?')
