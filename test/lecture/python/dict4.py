character = {
    'name':'기사',
    'level':12,
    'items': {
        'sword':'불꽃의 검',
        'armor':'풀플레이트'
    },
    'skill': ['베기', '세게 베기', '아주 세게 베기']
}

for keys in character:

    if type(character[keys]) is str or type(character[keys]) is int:
        print(f"{keys} : {character[keys]}")

    else:

        if type(character[keys]) is list:
            for i in range(len(character[keys])):
                print(f"{keys} : {character[keys][i]}")

        else:
            for key, val in character[keys].items():
                print(f"{key} : {val}")

