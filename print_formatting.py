#various ways to format your print statements
#one method of putting the variables into string

s = 'String'
print 'Place my variable here: %s' %(s) #results: Place my variable here: String

#the more specific to floating numbers
print 'Floating point number: %1.3f' %(13.145) #Floating point number: 13.145

#conversion formats, converts python mthds into a string
Print 'Convert to string %r' %(123) #convert to string: 123 #print formatting options, %r%s

#using multiple formats alot
print 'First: %s, Second: %s, Third: %s' %('hi', 'two', 3) #First: hi, second: two, Third: 3

#best wat to do this is to use string.format method in a more pythonic way
print 'First: %s, Second %s' %(2,2) #First: 2, Second:2

print 'First: {x}, Second: {y}, Third: {x}'.format(x='inserted', y='two') #First: inserted, second: two, third: inserted

#In python 3
print ('one: {x}'.format(x='INSERT!')) #one: INSERT!






