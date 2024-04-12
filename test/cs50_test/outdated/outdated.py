months_str = [
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

months_num=[1,2,3,4,5,6,7,8,9,10,11,12]

months = dict(zip(months_num, months_str))

#print(months)
while True:

    try:

        date = input("Date: ")
        if '/' in date or (' ' and ',') in date:
            date=date.replace('/',' ').replace(',','')
            if ' ' in date:
                date=date.split(' ')
                s_month=date[0]
                s_day=int(date[1])
                s_year=int(date[-1])

                if s_day>31:
                    break

                if s_month.isalpha():
                    months = dict(zip(months_str, months_num))
                    if s_month == list(months.keys())[int(months[s_month])-1]:
                        print(f"{s_year}-{int(months[s_month]):02}-{s_day:02}")
                        break
                    # else:
                    #     break
                else:
                    
                    if int(s_month) == list(months.keys())[int(s_month)-1]:
                        print(f"{s_year}-{int(s_month):02}-{s_day:02}")
                        break
                    # else:
                    #     break


            else:
                pass
        else:
            break
    except ValueError:
        break
    except Exception:
        pass
