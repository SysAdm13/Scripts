val1 = 53453
val2 = 4345345
str = '{0},{1}{0}'.format(val1,val2)
str1= '{val2}, {val1}, ' .format(val1=3, val2=4)
print(str)
print(str1)
print(", ".join(["Hello", "my", "world"]))
#prints "Hello, my, world"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is Wold.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"