def main():
    x = get_int("what's x: ")
    y = get_int("what's y: ")
    print(f"x is {x}")
    print(f"y is {y}")

def get_int(question):
    while True:
        try:
            return int(input(question))
        except ValueError:
            pass
        else:
            break

main()
