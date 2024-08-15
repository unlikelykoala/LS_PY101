str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def da_end(text):
    if text.endswith('!'):
        print(True)
    else:
        print(False)

    if text[-1] == '!':
        print(True)
    else:
        print(False)

da_end(str1)
da_end(str2)
