tel = {'jack': 4098, 'sape': 4139}

print("before: ", tel)

tel["guido"] = 4127

print('after: ', tel)

del tel['sape']

print("after: ", tel)

print(list(tel))
print(sorted(tel))

if 'jack' in tel:
    print("Yes")
if 'sape' not in tel:
    print("Nope")

