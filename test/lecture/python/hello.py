# start the function again, from #Def
def main ():
    name = input("What's your name? ")
    print(name)
    hello(name)
    hello()


def hello(var="world"):
    print("Hello", var)



main()



