name_for_userid = {
382: 'Alice',
590:"Bob",
951:"Dilbert"
}

def greeting(userid):
    #.get() returns value if key  exists otherwise it returns None or default
    return "Hi %s!" % name_for_userid.get(userid,"there")

greeting(590)
greeting(433)

#............................................................................................

# 'is' vs '=='
a = [1,2,3]
b = a

a is b # "is expression evalutes to true if two variables points to same object"

a == b # '== evalutes to true if the objects referred to by the variables are equal'

c = list(a)

a==c # a and c refrer to same variable

a is c

#...........................................................................................

def myfunc(a,b):
    return a+b

funcs = [myfunc]
funcs[0]
funcs[0](2,3)

#..........................................................................................

def dipatch_if(operator, x, y):
    if operator == 'add':
        return x+y

    elif operator == 'sub':
        return x-y

    elif operator == 'mul':
        return x*y

    elif operator == 'div':
        return x/y

    else:
        return None

def dispatch_dict(operator, x, y):
    return {
    'add': lambda: x+y,
    'sub': lambda: x-y,
    'mul': lambda: x*y,
    'div': lambda: x/y,
    }.get(operator, lambda : None)() # dictionary.get("search for key", default)


dipatch_if('add', 2,4)
dispatch_dict('sub',4,6)
dispatch_dict('module',4,5)
#........................................................................................
'''
syntax:
vals = [expression for value in collection if condition]
the above syntax is equal to below code

vals =[]
for value in collections:
    if condition:
        vals.append(expression)

#look below example
'''
even_squares = [ x * x for x in range(10) if not x%2 ]
even_squares

#...........................................................................................
'''
variable = [start, end, skip]

'''
string = 'hello python.learning'
# string reverse
string[::-1]
# reversing reversed string
string[::-1][::-1]
# skip one character
string[::2]
# skipping two characters
string[::3]
# strating from not first string
string[2::-1]
string[3::-1]
string[4::-1]

#..............................................................................................

my_list = [1,2,3,4,5]
# clear all elements in a my_list
del my_list[:]
my_list

#del my_list will delete my_list variable instance

#you can replace all elements in a my_list
#without creating a new list object
a = my_list

my_list[:] = [7,8,9]
my_list
a
 a is my_list

# you can also create a shallow copy of list

 b= my_list[:]
 b
 b is my_list
 #.......................................................................................

import collections
sting = 'hi there, this is going to be fun you can love it'

c = collections.Counter(sting)

c.most_common(1)
c.most_common(4)

for i in c:
    print(i, c[i])

#.........................................................................................

import itertools
for p in itertools.permutations('HT'):
    print(p)
for p in itertools.permutations('APPLE'):
    print(p)

itertools.combinations([1,2,],2)
list(itertools.combinations([1,2,3,],2))

#..........................................................................................
import cv2
import matplotlib.pyplot as plt
# load the image with imread
img = cv2.imread('123.jpg')
plt.imshow(img)
# flipping image horizontally, vertically, both_axes
horizontal_img = cv2.flip(img, 0)
plt.imshow(horizontal_img)
vertical_img = cv2.flip(img, 1)
plt.imshow(vertical_img)
both_img = cv2.flip(img,-1)
plt.imshow(both_img)
#...................................................................................
import nltk
nltk.download()

from textblob import TextBlob
# string
stin = TextBlob('heloo this is new prograaming languaage')
stin
# correcting the textblob
stin.correct()

stin.word_counts
TextBlob('我爱你').detect_language()
TextBlob('').translate()
TextBlob('').translate.lower()

stin.pos_tags

#.....................................................................................

a= 'hello python'
b ='hello python.learning'
# getting unique words
set(a)
# sorted return all keys in sorted
sorted(set(a))

# intersection to find common in between them

set(a).intersection(set(b))
# symmetric difference will returns mismatched keys
set(a).symmetric_difference(set(b))

# union returns all unique keys
set(a).union(set(b))

#.......................................................................................

import platform
# information about architecture
platform.architecture()
# which bit
platform.machine()

# returns platform of machine
platform.platform()
platform.processor()
platform.system()
platform.uname()
#.......................................................................................

a =['a','b','c','d','e']
b =[1,2,3,4,5]

#adding multipule list
a+b
max(a)
max(b)
min(b)
min(a)
# sorted returns sorted list
sorted(a)
sorted(b)
a.count(1)
a.count('b')
a.extend(b)
a

a = [')','(','!','@','$','&']
sorted(a)
#........................................................................................

# generting even and odd using lambda

a = list(range(1,16))
a
# return lambda value which is x%2!=0

odd = list(filter(lambda x: x%2, a))
odd

even = list(filter(lambda x: x%2 == 0, a ))
even

#.......................................................................................

def mul(a):

    return 2*a

s =(1,2,3,4,5,6,7,8,'hello')
list(map(mul, s))

#........................................................................................
import phonenumbers
# put arguments with countrycode
x = phonenumbers.parse("+918985407817")
x

phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL)
phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
phonenumbers.parse('+918985407817')

from phonenumbers import carrier
from phonenumbers import parse
carrier.region_code_for_number(parse('+918985407817'))
#.....................................................................................
import matplotlib.pyplot as plt

data = {'player':['messi','ronaldo','Isco','dravid'],
'goals':[15,20,45,78],
'assists':[12,8,14,5],
'mistakes':[2,4,3,5],
'shoots':[243,233,33,43]
}

fig = plt.figure('player Graph')
ax = fig.add_subplot(1,1,1)
bar_width =0.5

bars =[i+1 for i in range(len(data['goals']))]
ticks = [i+(bar_width/2) for i in bars]
#........................................................................................

from bs4 import BeautifulSoup
from requests import get

url = 'https://www.tutorialspoint.com/python/'
response = get(url)
content = response.content
content
soup = BeautifulSoup(content, 'lxml')
soup.prettify

parse_data = soup.find_all('h3',{'class':'sreading'})
parse_data
for i in parse_data:
    link_name = i.textblob
    link = i.find('a')['href']
    print(link, '...>', link_name)

#.......................................................................................

import random

random.randrange(6)

random.random()
random.random()

# choice return any one from interable

random.choice([2,4,5,'hello','python.learning'])
# sample returns list of given random numbers
random.sample([1,2,3,4,5,6,7],4)
#....................................................................................
import turtle

trt1 = turtle.Turtle()
# set background color
turtle.bgcolor('Black')
trt1.speed(0)
#title of your design
turtle.title('Design')
def drawrainbow():
    for i in range(500):
        trt1.color('white') #color of pointer pen
        trt1.backward(i) # go backward side with growing
        trt1.left(110) # turn 110 degrees left
    trt1.color('white')
    trt1.hideturtle()
    trt1.setpos((20,0))
drawrainbow()

#.......................................................................................
class calc:
    def __init__(self):
        self.num1 = 100
        self.num2 = 200
    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2


c = calc()
c.add()
c.sub()
#.........................................................................................
import cv2
cv2.imread('123.jpg')
type(cv2.imread('123.jpg'))
import matplotlib.pyplot as plt
image_array = cv2.imread('123.jpg')
plt.imshow(image_array)
plt.show()

#........................................................................................

def add(a,b):
    return a+b

def power(a,b):
    return a**b

flag = True
print((add if flag else power)(3,2))
print((add if not flag else power)(3,2))

#.......................................................................................

a=4
#chained comparison
print(2 < a < 8)
print(1 == a <10)

# transposition of 2*3  into 3*2
matrix = [[1,4],[2,5],[3,6]]
transpose = zip(*matrix)
tuple(transpose)


#os module
import os
from os import path
os.listdir()
dic ={'a':0, 'b':1}
dic
dic['a']
dic.get('c', 4)
dic.__setitem__('c',2)
dic

dic.update({'d':3})
dic
dic.pop('a')
dic

#input i have given to you
a ="[1,2,3,4]"
type(a)
#source code:
#below code converting my string list to list
s = eval(a)
s
#look below
type(s)

# dictionary in a string
a = '{"senha": 100}'
type(a)
s = eval(a)
s
type(s)

import emoji

v = ord('😀')
v

s= chr(128512)
s


a =[[10,20,30],[30,40,50], [70,80,90]]

for i in range(len(a)):
    print(i)
    for j in range(len(a[i])):
        print(a[i][j], end =" ")
    print()


0.5**2

1-0.5**2

import matplotlib.pyplot as plt
import numpy as np

def gini(p):
    return (p)*(1-p) + (1 - p)*(1-(1-p))

def entropy(p):
    return -p* np.log2(p) - (1-p)*np.log2(1-p)

def error(p):
    return 1 - np.max([p, 1 - p])

x = np.arange(0, 1.0, 0.01)

ent = [entropy(p) if p != 0 else None for p in x]

sc_ent = [e*0.5  if e else None for e in ent]

err = [error(i) for i in x]

fig = plt.figure()
ax = plt.subplot(111)

for i, lab, ls,c in zip([ent, sc_ent, gini(x), err],
['Entropy', 'Entropy(scaled)', 'Gini Impurity', 'Misclassification error'],
['-','-','-.','--'],['black','lightgray','red','green','cyan']):
    line = ax.plot(x,i, label= lab, linestyle=ls, lw=2, color=c)

ax.legend(loc='upper center',bbox_to_anchor=(0.5,1.15),
ncol=5,fancybox=True, shadow = False)
ax.axhline(y=0.5, linewidth=1, color='k', linestyle = '--')
ax.axhline(y=1.0, linewidth=1, color='k', linestyle = '--')
plt.ylim([0,1.1])
plt.xlabel('p(i=1)')
plt.ylabel('Impurity Index')
plt.show()
import seaborn as sns

data = sns.load_dataset('iris')
data.head()
X = data.iloc[:,:-1].values
X
y= data.iloc[:,[4]]
y
from sklearn.model_selection import train_test_split
x_train, x_test,y_train, y_test = train_test_split(X,y)

from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(max_depth=4,random_state=1)
tree.fit(x_train,y_train)
y_pred = tree.predict(x_test)
y_pred

from sklearn.metrics import accuracy_score

metric = accuracy_score(y_test,y_pred)
metric

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test,y_pred)
cm

from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz

dot_data = export_graphviz(tree, filled=True,rounded=True,
class_names=['Setosa','Versicolor','Virginica'],feature_names=['sepal lenth','sepal width','petal_length','petal_width'],
out_file=None)

graph = graph_from_dot_data(dot_data)
graph.write_png('data')

#..........................................................................................

a =[1,2,3,4]
b=(5,6,7,8)
c=[9,10,11,12]

def func(*args):
    for i in a:
        print(i)
    for j in b:
        print(j)

    for k in c:
        print(k)

func(a,b,c)
