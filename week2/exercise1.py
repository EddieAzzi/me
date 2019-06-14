"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
#A list of words is used to show what "some_words" is equal to. e.g. an example of "some words" would be "does" and "line".
some_words = ['what', 'does', 'this', 'line', 'do', '?']

#This will print a single word in the list above.
for word in some_words:
    print(word)

#This will print a number (labelled as "x") of words from the list above.
for x in some_words:
    print(x)

#This will print every word in the list above. Possibly creating the sentence, "what does this line do?". OR this will simply print "some_words", which equals to the list.
print(some_words)

#The amount of elements in the list is greater than 3. If a word contains more than 3 words, it will print the word.
if len(some_words) > 3:
    print('some_words contains more than 3 words')

#The useful function is defined by the returned tuple. This is then printed.
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

#The useful function 
usefulFunction()
