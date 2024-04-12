'''
text=input("Input: ")

for char in text:
    llw=char.lower()
    if llw=='a' or llw=='e' or llw=='i' or llw=='o' or llw=='u':
        text=text.replace(char, '')


print(f"Output: {text}")
'''
#------------------------------

vowels = ['a','e', 'i', 'o', 'u']

text = input("Input: ")

print("Output: ", end='')
for c in text:
    if c.lower() not in vowels:
        print(c, end='')

print()
