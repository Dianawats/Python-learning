l = []
for letter in 'word':
    l.append(letter)
print l
#results
['w','o','r','d']

#build the above out using list comprehension
lst = [letter for letter in 'word'] #syntax for list comprehensions
lst
['w', 'o','r','d'] #results are the same

lst = [x**2 for x in range(0,11)]
lst
[0,1,4,9,16,25,36,49,64,81,100] #results

lst = [number for number in range(11) if number % 2 == 0] #list comp to print only even numbers
lst
[0,2,4,6,8,10] #results even numbers

#list comp using a forloop
lst = []
for number in range(11):
    if number %2 ==0:
        lst.append(number)

lst #results
[0,2,4,6,8,10]

#complicated example convert from celsius tp farenheit
celsius = [0, 10, 20.1, 34.5]

farenheit = [(temp * (9/5.0 + 32) for temp in celsius ]

farenheit #results
[32.0, 50.0, 68.18, 94.1 ]

#nested list comprehension
lst = [x**2 for x in range(11)]
lst #results
[0,1,4,9,16,25,36,49,64,81,100]  #power of two

lst = [x**2 for x in [x**2 for x in range(11)]] #power of four
lst #results
[0,1,16,81,256,625,1296,2401,4096,6561,10000]

#Assignment
#Qn 1. Use for, split() and if to create a statement that will print out letters that start with s in this sentence
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print word
    # start
    # s
    # sentence, results

#qn 2. use range() to print all the even numbers from 0 to 10
range(0,11,2)
[0,2,4,6,8,10] #results

#qn3. Use list comprehensions to create alist of all numbers btn 1 and 50 that are divisible by 3
[x for x in range(50) if  x  %3 == 0]
[0,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48]

#qn4. write a program that prints the integers from 0 to 100. But for three multiples of three
#print "Fizz", instead of the number and for the multplies of five print "Buzz". For numbers which
#are multiples of both three and five print "fizzbuzz"
for num in xrange(1,101):
    if num % 5 == 0 and num % 3 == 0:
        print "fizzbuzz"
    elif num  % 3 == 0:
        print "fizz"
    elif num % 5 == 0:
        print "buzz"
    else:
        print num

 #qn4. Use list comprehension to create a list of the first letters of every word in the string below:
 st = 'Create a list of first letters of every word in this string'
 [word[0] for word in st.split()]
 ['C', 'a', 'l', 'o', 'f', 'l', 'o', 'e', 'w', 'i','t', 's'] #results

 






