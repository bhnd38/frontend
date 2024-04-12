a=input("camelCase: ").strip()
i=0
for i in range(len(a)):
    if a[i].islower()==False:
        low=a[i].lower()
        a=a.replace(a[i], "_"+low)
    # elif i==len(a):
    #     break
print(a)
