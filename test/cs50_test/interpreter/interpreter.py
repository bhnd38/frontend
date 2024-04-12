x, y, z=input('Expression: ').split(" ")

if y=='+':
    a=float(x)+float(z)
elif y=='-':
    a=float(x)-float(z)
elif y=='/':
    a=float(x)/float(z)
    a=f"{a:.2f}"
elif y=='*':
    a=float(x)*float(z)
else:
    print("It's wrong. please check")
print(a)
