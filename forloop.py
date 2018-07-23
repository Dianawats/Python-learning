#forloop statement
l = [1,2,3,4,5]
l, #results [1,2,3,4,5]

for element in l:
    print 'element'
#results 
1
2
3
4
5

for num in l:
    print 'something!'
#results
something!
something!
something!
something!
something!

#MODULO getting the remainder in division, it uses %symbol
#super basic kind of elementary division
10 % 3 #results 1, because one is the remainder
4 % 2 #results 0

#prints only even numbers
l, #results [1,2,3,4,5]
for num in l:
    if num % 2 ==0:
        print num
#results, prints 2, 4 . It prints only even numbers

for num in l:
    if num % 2 == 1:
        print num
#results, prints 1,3,5. it prints odd numbers

for num in l:
    if num % 2 == 0:
        print 'Here is an even'
    else:
        print 'Odd number'
    #results, 
    # Odd number!
    # Here is an even
    # Odd number!
    # Here is an even

for num in l:
    if num % 2 == 0:
        print num
    else:
        print 'Odd number!'
    #results, 
    # Odd number!
    # 2
    # Odd number!
    # 4
    #Odd number!

    #Forloop that sumsup that list
    l, [1,2,3,4,5]
    list_sum = 0
    for num in l:
        list_sum + num
    print list_sum
    #results, 15

    #forloop using string, it will index
    s = 'this is a string'
    for letter in s:
        print letter
        #results
        t
        h
        i
        s

        i
        s

        a

        s
        t
        r
        i
        n
        g
#forloops in a tuple, u can also call t, whatever u want to call it
tup = (1,2,3,4,5)
for t in tup:
    print t
    #results
    1
    2
    3
    4
    5
#Advanced, tuple unpacking
#We gonna create a list of tuples, create some tuple pairs in a list









