x = 0
while x<10:
    print 'x is currently: ', x
    x += 1
    #results
    # x is currently: 0
    # x is currently: 1
    # x is currently: 2
    # x is currently: 3
    # x is currently: 4
    # x is currently: 5
    # x is currently: 6
    # x is currently: 7
    # x is currently: 8
    # x is currently: 9

 x = 0
while x<10:
    print 'x is currently: ', x
    x += 1
else:
    print 'All done!' 
    #results
    # x is currently: 0
    # x is currently: 1
    # x is currently: 2
    # x is currently: 3
    # x is currently: 4
    # x is currently: 5
    # x is currently: 6
    # x is currently: 7
    # x is currently: 8
    # x is currently: 9
    # All done!

    #Break, continue and pass
    #we use them to add aditional functionality for various cases 
x = 0

while x < 10:
    print 'x is currently: ', x
    print 'x is still less than 10, adding 1 to x'
    x += 1

    if x == 3:
        print 'x is equal to 3!' 
        break
    else:
    print 'Continuing .....'
    continue
#results #it does not continue going because of the break

# x is currently: 0
#  x is still less than 10, adding 1 to x
# continuing .....
# x is currently: 1
#  x is still less than 10, adding 1 to x
# continuing .....
# x is currently: 2
#  x is still less than 10, adding 1 to x
# x is equal to 3!



