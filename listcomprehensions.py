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


