# # No Duplicates

# Input: a string of words separated by spaces. Only the letters `a`-`z`
# are utilized.

# Output: the string in the same order, but with subsequent duplicate
# words removed.

# There must be no extra spaces at the end of your returned string.

# The solution must be `O(n)`.


def no_dups(s):
    # Your code here

    key_str = ""
#  .split turns string into a list
    words = s.split()
    # create dictionary
    dict_keys = dict() 
    # going through words
    for item in words:
        # logic for only showing words that have not appeared
        if item not in dict_keys.keys():
            dict_keys[item] = item 
            key_str += item + ' '
     
    return key_str.strip()  # removes beg & end spaces in string

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))