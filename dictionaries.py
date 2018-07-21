#mappings in python
#Mappings are collection of objects that are stored by a key
#Python dict consists of a key, then associated value
my_dict = {'key1':'value', 'key2': 'value2' }
my_dict['key1']
value #results

my_dict = {'k1':123, 'k2':3.4, 'k3':'string'}
my_dict['k3'].upper
STRING #results

#We can also affect the value and key as well
my_dict['k1'] - 120
my_dict['k1']
3 #results

#gives the same answer like the above but different method
my_dict['k1'] +=100
my_dict['k1']
203 #results

#Adding new keys and new values
d = {}
d # u get {}
d['animal'] = 'Dog'
d['answer'] = 42
d #results u get {'animal': 'Dog', 'answer': 42}

#nesting with dictionaries, dictionary inside the dictionary
d = {'k1': {'nestkey': {'subnestkey': 'value'}} }
d #results {'k1': {'nestkey': {'subnestkey': 'value'}}}
d['k1']['nestkey']['subnestkey'].upper()
VALUE #results

#Dictionary methods that are built in
d{}
d['k1'] = 1
d['k2'] = 2
d['k3'] = 3
d #results {'k1': 1, 'k2': 2, 'k3':3} #full mapping
d.keys()
['k1', 'k2', 'k3'] #returns all the keys
d.values()
['1,2,3'] #returns all the values
#we can index strings and lists but not dictionaries
#Dictionaries call things by its key

#if u want a combination
d.items()
[('k3',3), ('k2',2), ('k1',1)] #it returns a tuple





 