# A function is a useful device that groups together a set of statements so they can be run more than once
#can also let us specify parameters that can serve as inputs to the function
# ALso allows us not to have repeatedly write the same code again and again
#Buiding blocks when constructing larger and amounts of codes to solve problems
#def inbuilt key word
def name_of_function():
    pass

#another example
def my_addition_func(arg1,agr2):
    print arg1 + agr2
my_addition_func(1,2)
3 #results

#docstring
def greetings(name):
    print "Hello" + name
    greetings ('Diana')
    Hello, Diana #results

  #the return statement, returns a result that can be stored as a variable
def greetings(name):
    print "Hello" + name
def add_num(num1, num2):
    return num1 + num2
print add_num(2,3)
5 #results

#we dont declare variable types in python, e.g var = 'int

#we gona use break, continue and pass 
#writing a docstring, it is a description of what's going on in a function
def is_prime(num):
    """
    This function checks for prime numbers
    """
    for n in range(2, num):
        if num % n ==0:
            print "not prime"
            break
    else:
        print "The number is prime"
is_prime(13)
#results will be: The number is prime
#if you put 12 where 13 is. It will print not prime

#using math or modules to check



    
  




