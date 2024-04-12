from pyfiglet import Figlet
import sys
import random
figlet = Figlet()
fonts=figlet.getFonts()
while True:

    try:
        text=input("Input: ")

        if len(sys.argv) < 2:
            figlet.setFont(font=random.choice(fonts))

        elif len(sys.argv) >= 2:
            figlet.setFont(font=sys.argv[-1])
            if sys.argv[1] != "-f" or sys.argv[1] != "--font":
                raise ValueError

        print(figlet.renderText(text))
        break


    except Exception:
        print("Invalid usage")
        sys.exit()
