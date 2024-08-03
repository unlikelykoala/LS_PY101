'''
Write a function that takes two strings as arguments, 
determines the length of the two strings, 
and then returns the result of concatenating the 
shorter string, the longer string, and the shorter string once again. 

You may assume that the strings are of different lengths.
'''

def short_long_short(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)
    if s1_len > s2_len:
        new = s2 + s1 + s2
        return new
    new = s1 + s2 + s1
    return new

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")
    