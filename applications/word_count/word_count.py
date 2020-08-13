# # Count the words in an input string

# ## Input

# This function takes a single string as an argument.

# ```
# Hello, my cat. And my cat doesn't say "hello" back.
# ```

# ## Output

# It returns a dictionary of words and their counts:

# ```
# {'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}
# ```

# Case should be ignored. Output keys must be lowercase.

# Key order in the dictionary doesn't matter.

# Split the strings into words on any whitespace.

# Ignore each of the following characters:

# ```
# " : ; , . - + = / \ | [ ] { } ( ) * ^ &
# ```

# If the input contains no ignored characters, return an empty dictionary.


def word_count(s):
    # Your code here
#     added list of characters to be ignored
     ignored_list = ['"', ':', ';', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
     
     # remove any ch in ignored_list and make s all lowercase
     for ch in ignored_list:
          s = s.replace(ch, "").lower()
      

     #  create dictionary
     count_dict = dict()
     #  .split turns string into a list
     word_list = s.split()

     for word in word_list:
          if word not in count_dict:
               count_dict[word] = 1
          else:
               # adds 1 if it already appeared
               count_dict[word] += 1     

     return count_dict


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))