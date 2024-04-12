def main():

    time = input("What time is it? ").split(":")

    if 7.0<=convert(time)<=8.0:
        print("breakfast time")
    elif 12.0<=convert(time)<=13.0:
        print('lunch time')
    elif 18.0<=convert(time)<=19.0:
        print('dinner time')
    else:
        None
# a, b=int(time[0]), int(time[1])
# if a==7:
#     print("breakfast time")
# elif a==8 and b==0:
#     print("breakfast time")
# elif a==12:
#     print("lunch time")
# elif a==13 and b==0:
#     print('lunch time')
# elif a==18:
#     print('dinner time')
# elif a==19 and b==0:
#     print('dinner time')
# else:
#     None


def convert(time):
    hour=float(time[0])
    minute=round(float(time[1])/60, 1)

    return hour+minute


if __name__ == "__main__":
    main()
