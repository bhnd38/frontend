import requests
import sys

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    if IndexError:
        if sys.argv[1].isalpha():
            print("Command-line argument is not a number")
            sys.exit()
        else:
             print("Missing command-line argument")
    else:
        rate=float(response.json()["bpi"]["USD"]["rate_float"])

        print(f"${int(sys.argv[1])*rate:,.4f}")

except requests.RequestException:
        print("오류 발생")
        sys.exit()
