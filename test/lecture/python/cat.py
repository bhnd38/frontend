def main():
    meow(user_input())

def user_input():
    while True:
        n=int(input("What's n? :"))
        if n>1:
            return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()
