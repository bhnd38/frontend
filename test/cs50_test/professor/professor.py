import random


def main():
    lvl=get_level()

    score = 0

    qcount = 0


    while qcount < 10:
        chance = 3
        X, Y = generate_integer(lvl)
        answer = int(input(f"{X} + {Y} = "))

        if answer == X+Y:
            score += 1
            qcount += 1
            continue

        else:
            while answer != X+Y:
                print("EEE")
                qcount += 1
                chance -= 1
                answer = int(input(f"{X} + {Y} = "))

                if chance == 1:
                    print()
                    print(f"{X} + {Y} = {X+Y}")
                    break



        if qcount == 10:
            break
    print(f"Score: {score}")



def get_level():
    while True:
        a = int(input("Level: "))
        try:
            if 1 <= a <= 3:
                return a
        except:
            pass



def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)

    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y

if __name__ == "__main__":
    main()



