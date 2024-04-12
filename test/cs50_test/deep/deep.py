text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
if text == "42" or text == 'forty-two' or text=='forty two':
    answer = "Yes"
else:
    answer = "no"

print(answer)

