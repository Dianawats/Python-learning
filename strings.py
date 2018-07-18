'Hello'
print 'This is also a string'
print "This is a string"

#\n stands for newline and \t is tab
print "Here is the first line \n and the other is the second line"

#length function len()
len("Hello world")

s = "Hello world"
print s

#indexing in python, used []
#indexing starts at 0
s[0] #it will print H

#slicing in python [1:] colon means it grabs onwards
s[1:] #it will grab 'ello world'

s[3:] #grab everything upto the third index, it gives 'Hel'

s[:] #grab everything it gives 'Hello world'

#indexing backward
s[-1] it gives 'd'

s[::-1] #it gives 'dlrow olleH', reversing the screen is common

#string properties, known as immutability. it means once the string is created, 
#elements can't be changed
#strings are immutable, you can just add on to them by concentenating (.)

s
'Hello world'
s + 'concentenate me'
#it gives "Hello world concentenate me"
#you can't change particular element, u just add on to it

#you can also reassign this
s = s + 'concantenate me' # u get the same statement above

#you can also use multiplication symbol
letter = 'z' #type letter, then it outputs z

letter * 10 # it will print z ten times like 'zzzzzzzzz'

#Objects in python have built in methods
#these mthds are just functions inside the objects
s = 'Hello'
s.upper() #it gives uppercase 'HELLO'
s.lower() #gives lower case







