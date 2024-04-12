import random



while True:
    try:
        num = int(input("Level: "))

        if num > 0 :
            break

    except ValueError:
        pass


a = random.randint(1, num)

while True:

    try:
        g = int(input("Guess: "))
        if g == a:
            print("Just right!")
            break
        elif 0< g < a:
            print("Too small!")
            pass
        elif g > a:
            print("Too large!")
            pass
        elif g < 0:
            pass

    except ValueError:
        pass

