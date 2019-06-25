#sets
# creating empty set
a =set()
a ={1,2,3,4,5}
type(a)
b={3,4,5,6,7}
type(b)

#Intersection
# intersection prints the common elemnets which are in a
a.intersection(b)

#unioun
# unioun prints all the elemnets but removes the multipule occurences
a.union(b)

#Difference
# prints the different elements from a which are not occured from b
a.difference(b)

# symmetric difference
# removes common elemnets from a and b, prints different elements from both and b
a.symmetric_difference(b)

#superset
a.issuperset(b)

#subset
a.issubset(b)
# disjoint

a.isdisjoint(b)

# with single element checking in sets

2 in a

5 not in b

# add and remove from set
# add
s ={1,2,3}

s.add(4)
s

s.remove(4)

#s.remove(5)# if the element is not in set it raises key error

# get unique elements from list

resturants = {'KFC', 'dominos', 'burger king', 'KFC'}
unique_resturants =  set(resturants)
unique_resturants

# listing all unique resturants in a list
list_unique_resturants =  list(set(resturants))
print(list_unique_resturants)

#s = {{1,2,3},{3,4,5}} # set of set gives unhasable error
# instead use frozenset
s = {frozenset({1,2}), frozenset({3,4})}
s

'''
sets are unorderd collection of distinct elements , but sometime swe want to work with
the unorder collection of elements that are not necessarily distinct and keep track of the elements
multiplicits
s ={'a','b','b','a'}
s

here we are loosing some information, i want all elements but order is not important

ofcourse saving elements to list would retain this information

list = ['a', 'b','b', 'a']

but list structure introduces unneeded structuring that will slowdown our computations

for implementing multisets python provides the counter class from the collection module
'''
from collections import Counter

counterA = Counter(['a','b','a','b'])
counterA

# counter is a dictionary where elements are stored as dictioanry keys and their
# count are stored as dictionary values , it is unorderd collection

# operator precedence in python
''' python have a set of order of precedence which determines what opertor are evaluated first

python follows PEMDAS rule . PEMDAS stands for parenthasis, exponents, multiplication, divison, and addition

'''
a,b,c,d = 2,3,5,7

a**(b+c)

a*b**c

# variable scope and binding
# nonlocal keyword adds a scope overrides to the inner scope
'''
def counter():
    num =0
    def incrementer():
        num+=1
        return num
    incrementer()

counter() # this code returns unbound local error
here num=0 we declared in outer function but we are incrementing in inner function
now num=o is behaves like a global if you want to perform calculations on that you ahve to use non local keyword
'''

def counter():
    num=0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer

c = counter()
c()
c()
c()

# global variable  and loacl variables

# variables which are declared inside function as local ,
# variable swhich are declared outside trhe function as global

x = 'hi'

def read_x():
    print(x) # here x is just refrenced , therefore assums as global
read_x()
'''

def read_x_local_fail():
    if False:
        x ='hey'
    print(x)

read_x_local_fail()
unbound local error
'''
x = 'hi'
def change_global_x():
    x ='bye'
    print(x)

change_global_x()
print(x)

#declaring the name global means that , for the rest of te scope it will changes
x = 'hi'
def change_global_x():
    global x
    x ='bye'
    print(x)

change_global_x()
print(x)

def a():
    v = 10
    return v
a()

print(v)    # it gives name error above v is local variable

def foo():
    if True:
            a =5
    print(a)

foo()

z =3
def bar():
    if False:
        z =5
    print(z)
bar()    # unbound local error

# ternary opertor
# ternary opertor is used for inline conditional expression

n= 5
" greater than 2" if n>2 else "smaller than or equals to 2"

# ternary opertor can also be nested

'hello' if n> 10 else 'good day ' if n>6 else 'bad day'


for i in range(0,4):
    print(i)
    if i == 2:
        break

def break_loop():
    for i in range(1,5):
        if i==2:
            break
        print(i)
    return(5)

break_loop()

def break_loop():
    for i in range(1,5):
        if i==2:
            return(i)
        print(i)
    return(5)

break_loop()

#........................................................................................
# dictionaries

d ={}
d = dict()

d={'key':'value'}
d
d = dict(key = 'value')
d
d=dict([('key','value')])
d

# adding new key and new value to the existing dictioanry
d['newkey'] ='new value'
d

# deleting newkey
del d['newkey']
d

# avoiding key error exception

#d['existedkey']
value = d.get('existedkey', 'it is not available')
value
d

# setdefault

d.setdefault('foo', 'bar')
d

# iterating over dictionary

for key, value in d.items():
    print(key, value)

for k in d.keys():
    print(k,d[k])

# dicitonary with default values

from collections import defaultdict
d = defaultdict(int)
d['new_key']
d['new_key']=5

d =defaultdict(lambda: 'empty')
d['existedkey']
d['key']=66
d

# merging dictionaries

fish ={'name':"Nemo", 'hands':'fins', 'special':'gills'}
dog = {'name':'clifford', 'hands':'pawns','color':'red'}

fishdog = {**fish, **dog}
fishdog

from collections import ChainMap

dict(ChainMap(fish, dog))

from itertools import chain

dict(chain(fish.items(), dog.items()))
# rules for  dictionary:
# every key must be unique(otherwise it will be overriden)
# every must be hasable(can use hash function to hash it


iterable = [('eggs', 5),('milk', 3)]
d = dict(iterable)
d

 #Or using keyword argument

d = dict(egg =10, maggie =5, dosa=12)
d

# creating orderd dictionary

from collections import OrderedDict
d = OrderedDict()
d['first']=1
d['second']=2
d

#.......................................................................................
# list
# LIST IS MUTABLE
# this can contain other type of objects
a = [1,2,3,4,5]
# append(value):
# appends a new element to the end of the list
a.append(6)
a
a.append([7,8,9])
a
a.append('mystring')
a

# extend(enumerable):
# extend the list by appending elements form another enumerable
a.extend([9,10,11])
a
a.extend([[10,12],13,[14]])
a

# index(value,[starting index])
# index returns the index position
a.index(4)
a.index(9)

#insert(index, value):
# insering value in particular index position
a.insert(6,7)
a
# pop([index])
#it removes and returns the item at index.
#With no argument it removes and returns the last element of the list
a.pop() # no argument
a

a.pop(7)
a

# remove(value):
# removes the first occurence of the specified value
#if the value cannot be found it raises the value error

# reverse():
# reverse the list in-place
a.reverse()
a

#count:
#count the number of occurence of some value in the list
a.count(10)
a

# sort():
#sort the list in numerical and lexicorgraphical
#a.sort(reverse = True) # error because my a contain both string and integers

a =[1,2,3,4]

a
a.sort()
a

a= ['bunny','jeevan']
a.sort()
a
a.sort(reverse = True)
a

import datetime

class Person(object):
    def __init__(self, name , birthday, height):
        self.name = name
        self.birthday = birthday
        self.height = height

    def __repr__(self):
        return self.name

l = [Person("jeevan ", datetime.date(1994, 10, 11), 175),
     Person("bhavani priyanka", datetime.date(1996, 4, 18), 160)]
l.sort(key=lambda item: item.name)
l
l.sort(key=lambda item: item.birthday)
l
l.sort(key=lambda item: item.height)
l

# Better way to sort using attrgetter and itemgetter
# Lists can also be sorted using attrgetter and itemgetter functions
#from the operator module. These can help improve readability and reusability

from operator import attrgetter, itemgetter
people = [{'name':'JEEVAN','age':20,'salary':2000},
          {'name':'BHAVANI','age':18,'salary':5000},
          {'name':'BUNNY','age':30,'salary':3000}]

by_age = itemgetter('age')
by_salary = itemgetter('salary')

people.sort(key=by_age)
people # it inplaced the age

people.sort(key=by_salary)
people # sorted by salary and also inplaced

# itemgetter can also be given an index.
#this is helpful if you want to sort based on indices of a tuple.
list_of_tuples = [(1,2), (3,4), (5,0)]
list_of_tuples.sort(key=itemgetter(1))
print(list_of_tuples)

# Use the attrgetter if you want to sort by attributes of an object,
person = [Person("jeevan ", datetime.date(1994, 10, 11), 175),
     Person("bhavani priyanka", datetime.date(1996, 4, 18), 160)]

person.sort(key=attrgetter('name'))
person
person.sort(key=attrgetter('height'))
person

# clear():
# claer removes all items in the list
a.clear()
a

#  Replication :
# multiplying an existing list by an integer
#will produce a largest list containg that many copies of the original

b = ['jeevan']*5
b

# element deletion:
# it is possible to delete the multipule elemnets froom the list using del

z = [1,2,3,4,5,6,7,8,9,10]
z
del z[::2]
z

del z[-1]
z

del z[:]

# copying :
# the default assignmnet '='  assigns a reference of the original list to the
#new name, that is the original name and new name both are pointing to the same list object
# changes made to any one of them changes the other

a =[1,2,3,4]
a
b = a
b

# another way of copying
old_list = [3,4,5,6]
new_list = old_list[:]
new_list
new_list.append(4)
new_list
old_list

# use copy module to copy
import copy
new_list = copy.copy(old_list)
new_list

#This is a little slower than list() because it has to find out the datatype of old_list first.

new_list = copy.deepcopy(old_list)
new_list#inserts copies of the objects found in the original.

#Obviously the slowest and most memory-needing method, but sometimes unavoidable.

#copy():
# RETURNS A ASHALLOW copy of the list
aa = a.copy()
aa

# Acessing the list values
lst = [1,2,3,4,5]
lst[0]
lst[1]

#Negative indices are interpreted as counting from the end of the list.
lst[-1]
lst[-2]
lst[-5]
# this is the functionality evivalent to
lst[len(lst)-1]

# avoid slicing
'''When lists are sliced the __getitem__() method of the list object is called,
with a slice object. Python has a builtin slice method to generate slice objects.
We can use this to store a slice and reuse it later like so'''

data = 'jeevan 22 2019'
name_slice=slice(0,6)
data[name_slice]

# checking if list is empty
lst = []
if not lst:
    print("list is empty")

# iterating over list
my_list = ['foo', 'bar', 'baz']
for item in my_list:
    print(item)
for (index, item) in enumerate(my_list):
    print('The item in position {} is: {}'.format(index, item))

# checking whaether an item is in list or not
lst = ['test', 'twest', 'tweast', 'treast']
lst
'test' in lst
'toast' in lst
'jeevan' not in lst

# concatenate and merge :

list1 =[1,2,3,4,5,6]
list2 = [3,4,5,6,7,8,[9,10],[11]]

merged = list1 + list2
merged

# zip :
# zip returns a list of tuples

alist = ['a1','a2','a3']
blist = ['b1','b2','b3','b4']

for a, b in zip(alist, blist):
    print(a, b)

# len:
# it determinest the length of the list

len(['one','two','three'])

# removing duplicate values from the list
n  = [1,2,2,333,33333,3,33,3,3]
unique = list(set(n))

#decorators
def super(f):
    return f

@super
def myfunction():
    print('this is secret function')

myfunction()

# the above function is equivalent to below function
my_function = super(myfunction)
my_function()

def disable(f):
    pass

@disable
def func():
    print('this is function')

func()
