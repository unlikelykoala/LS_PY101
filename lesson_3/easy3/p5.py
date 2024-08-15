def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False

def color2(color):
    return color == 'blue' or color == 'green'

print(color2('yellow'))
print(color2('green'))
