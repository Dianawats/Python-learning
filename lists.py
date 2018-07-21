#lists hold different object types
my_lists = [1,2,3] # my_list. 123

len(my_lists) #4

#Slicing and indexing
my_lists = ['one', 'two', 'three', 4, 5]
my_lists[0] #you get 1

my_lists[1:] #['two', 'three', 4, 5]
my_lists[:3] #['one', 'two', 'three']

#adding item on the list
my_lists = my_lists + ['permanent add'] #my_lists, 'one','two','three',4,5,'permanent add'

#methods for lists
#append method
l = [1,2,3]
l.append('append me!') #l, u get [1,2,3,'append me!']

#pop method pops off the last object in a list
l.pop()
'append me!' #it returns [1,2,3]

x = l.pop(0) #x u get 1, then l, u get [2,3]

#sort and reverse
new_list = ['a', 'e', 'x', 'b', 'c']
new_list.reverse()
new_list #u get ['c','b','x','e','a']

#sort
new_list.sort()
new_list # it gives ['a','b','c','e','x']

#supports nesting, u can have data structures within data structures
#we going to do a list inside alist
#nesting data structures
l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]
matrix = [l_1, l_2, l_3]
matrix #[[1,2,3], [4,5,6], [7,8,8]] #lists inside the lists

#grab two elements, items inside the matrix object and items inside the lists
matrix[0] #it returns [1,2,3]
#grab the first objects in the matrix and grab in the list also
matrix[0][1] #u get 2
matrix[1][1] #u get 5
matrix[2][0] #it gives 7

#list comprehensions
#for every row in the matrix, grab the zero index
first_col = [row[0] for row in matrix]
first_col #u get [1,4,7]


