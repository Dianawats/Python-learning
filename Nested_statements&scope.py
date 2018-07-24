#creating a variable name in python, the name stored is called namespace
#Variable names also have scope determines the visibility of other names to other parts of your code
x = 25

def printer():
    x = 50
    return x

print x
print printer()

print x, is 25 #results
print printer() is 50 #results

#name assignment s will create or change local names by default
#Name references search (atmost) four scopes: local, enclosing functions, builtin and global

#local variable: names assigned in any way within a function (defor lambda) & not declared global within that function

#Enclosing functions local: Name in the local scope of any and all enclosing functions (def/ lambda) from inner to outer

#GLobal (module): Names assigned at the top level of a module file , or declared in a def within a file

#Built in (Python): Names preassigned in the builtin names module; open range(), syntax error.etc

#Local example
#x is local here
f = lambda x:x**2

#Enclosing function local
name = 'This is a global'
def greet():
    #Enclosing function
    name = 'Sammy'

    def Hello():
        print 'Hello ' +name

        Hello()
    greet()
    Hello Sammy #results

#global
print name
This is global name #results

#Built in
len
<function len>

#local example still
x = 50

def func(x):
    print 'x is', x
    x = 2
    print 'changed local x to', x

func (x)
print 'x is still', x

x, is 50 #results
changed local x to 2
x is still 50 #results

#global statement
x = 50

def func():
    global x
    print 'This function is now using the global x!'
    print 'Beacause of the global x is: ', x #50 
    x = 2
    print 'Ran func()', changed global x: to', x #50
print 'Before calling func(), x is: ', x #results 50
func()
print 'Value of x(out side of func()) is: ', x #results 2

#Everything in python is an object







