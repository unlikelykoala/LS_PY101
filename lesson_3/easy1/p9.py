import re

advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
word = 'house'
pattern = re.compile(r"\b" + word + r"\b")
match = pattern.search(advice)
index = match.start()
print(index)
print(advice[:index])

lst = advice.split()
index = lst.index(word)
print(' '.join(lst[:index]))

print(advice.split("house")[0])
