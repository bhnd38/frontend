while True:

    try:

        gauge = input("Fraction: ")

        x = int(gauge.split('/')[0])
        y = int(gauge.split('/')[-1])

        if 0.01 < x/y < 0.99:
            print(f"{int((x/y)*100)}%")
            break
        elif 0.99 <= x/y <= 1:
            print("F")
            break
        elif 0 <= x/y <= 0.01:
            print("E")
            break

    except (ValueError, ZeroDivisionError):
        continue
