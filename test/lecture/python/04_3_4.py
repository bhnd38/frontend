max_value = 0
a = 0
b = 0

for i in range(1,100//2+1):
    j = 100 - i

    if max_value < i*j:
        a=i
        b=j
    else:
        max_value=i*j

        print(f"최대가 되는 경우: {a} * {b} = {max_value}")

