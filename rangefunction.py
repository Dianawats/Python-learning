#range allows us to create a list of numbers from a starting point to the end
#in py3 range() behaves as a generator, means if u want to store a huge number in the memory
range(0,10) #or u can say range(10) get the same results
[0,1,2,3,4,5,6,7,8,9]

type(x) #u can also check type by doing that, it will result list.

start = 5
stop = 20
range(start, stop) #results [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

for num in range (10):
    print num
    #results will be
    0
    1
    2
    3
    4
    5
    6
    7
    8

    for num in xrange (10):
        print num
        #results , same results. But for xrange helps to save memory or used on huge data

