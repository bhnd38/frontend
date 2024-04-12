limit = 1000
i = 1
sum_value=0

while sum_value < limit:
    sum_value+=i
    i+=1



print(f"{i-1}을 더할 때 {limit}을 넘으며 그때의 값은 {sum_value}입니다")
