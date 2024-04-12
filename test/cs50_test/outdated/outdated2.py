months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date=input("Date: ")

        if '/' in date:
            mm, dd, yyyy=date.split('/')
            if 0<int(mm)<13 and 0<int(dd)<32:
                print(f"{yyyy}-{int(mm):02}-{int(dd):02}")
                break
            else:
                pass

        elif ' ' in date:
            mmdd, yyyy=date.split(' ')
            if ',' in date:
                mm, dd = date.split(',')
                print(f"{yyyy}-{months.index(int(mm))-1:02}-{dd:02}")
        else:
            pass
    except Exception:
        pass
