statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

def tcount(text):
    i = 0
    for letter in text:
        if letter == 't':
            i += 1
    print(i)

tcount(statement1)
tcount(statement2)
