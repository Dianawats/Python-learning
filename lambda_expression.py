#allows us to create "anonymous" functions
#This basically means that we can quickly make adhoc function s without needing to properly define a function using def
#it is a single expression, not a block of statements
#it is most useful for beginners
def square(num):
    result = num**2
    return result

    square(2)
    4 #results

def square(num):
    return num**2

    square(4)
    16 #results

    #putting all this into one line, another format
    def square(num): return num**2
    
    square(3)
    9 #results

#Converting square expression into lambda
square2 = lambda num: num ** 2
square2(10)
100 #results

#check if the number is even
even = lambda num: num%2 == 0
even(4)
True #results, check whether the number is even.

#using function
def even(num):
    return num%2 == 0
    even(10)
True #same results

#I want to make a function that grabs the first character of a string
first = lambda s: s[0]
first('Hello')
'h' #results

#How to reverse the string
rev = lambda s:[::-1]
rev('Hello')
'olleh' #results, reversed the string

#little advanced
def adder(x,y):
    return x+y
adder(10,12)
22 #results

#lets turn the above function into lambda expression
adder = lambda(x,y): x+y
adder(30,30)
60 #results

#Lambda(): these expressions are used in the conversion of map(), filter() and reduce()



