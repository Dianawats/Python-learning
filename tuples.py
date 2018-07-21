#Tuples are like lists, though they're immutable cannot be changed
#mostly they're used to things that can't change like days of the week, or dates on calendar
t = (1,2,3)
t # results 1,2,3

#checking the length
len(t)
3 #results, How many elements are in the tuple

#They also mix object types like lists
t = ('one', 2)
t #'one',2 results

#It also a sequence just like a list, it can be indexed
t[0]
'one' #results
t[1] #2 results

#tuple methods (index)
t.index('one')
0 #results

t.index(2)
1 #resuts

#.count, counts the number of times the value appears
#How many times the number appears in the tuple
t.count('one')
1 #results

t = (1,1,2,3,4)
t.count(1)
2 #results

t = (1,2,3)
t[0] = 's'
error #results because they are immutable u cannot assign s like lists where u get ['s', 2, 3]
#tuples has two methods 1. count and 2. index. Where as the list has many like append, sort etc.



