munsters_description = "The Munsters are creepy and spooky."

new = []
i = 0
for letter in munsters_description:
    if letter.isupper():
        new.append(letter.lower())
    else:
        new.append(letter.upper())

print(''.join(new))

print(munsters_description.swapcase())
