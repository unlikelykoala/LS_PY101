def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) == 4:
        for num in dot_separated_words:
            if not is_an_ip_number(num):
                return False
        return True
    return False
