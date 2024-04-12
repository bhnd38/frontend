numbers = [1,5,3,2,1,3,2,4,1,7,9,7,45,5,7,9,9,8,9,7,9,6,5]
counter={}
for number in numbers:
    if number in counter:
        counter[number]+=1
    else:
        counter[number]=1
print(counter)
