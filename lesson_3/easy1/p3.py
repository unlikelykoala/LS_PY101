famous_words = "seven years ago..."

new = 'Four score and ' + famous_words
print(new)

lst = famous_words.split()
newlst = ['Four', 'score', 'and']
new2 = ' '.join(newlst + lst)
print(new2)
