import datetime

now = datetime.datetime.now()

print(now)

if now.hour < 12:
    print(f"현재 시각은 {now.hour}시 {now.minute}분으로 오전입니다")

else:
    print(f"현재 시각은 {now.hour}시 {now.minute}분으로 오후입니다")
