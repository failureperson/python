# list data type
lis = [123, "abcd", 10.2, "d"]
lis1 = ["hello", "world"]
lis[0:2]  # it return 0 and 1 index
lis1 * 2
lis + lis1


# date and time :
# parsing a string into a time zone
import datetime
dt = datetime.datetime.strptime(
    "2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
dt
import dateutil.parser  # it is an external library
dt = dateutil.parser.parse("2016-04-15T08:27:18-0500")
dt

# constructing timezone aware datetime

from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9))
JST
dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo=JST)
dt
dt.tzname()

from datetime import datetime
from dateutil import tz

local = tz.gettz()  # get local time
PT = tz.gettz('US/Pacific')  # get Pacific time

dt_1 = datetime(2015, 1, 1, 12, tzinfo=local)
dt_1
dt_pst = datetime(2015, 1, 1, 12, tzinfo=PT)
dt_pst


# computing the time difference

from datetime import datetime, timedelta

now = datetime.now()

then = datetime(2016, 5, 23)

delta = now - then
delta
delta.days
delta.seconds

# Date Formating

# Time between two date-times

from datetime import datetime
a = datetime(2016, 10, 6, 0, 0, 0)
b = datetime(2016, 10, 1, 23, 59, 59)

a - b

(a - b).total_seconds()

# counting number of elements and store them as dictionaries


from collections import Counter
counterA = Counter(['a', 'b', 'b', 'c'])
counterA


# variable scope and binding

def counter():
    num = 0

    def incrementer():
        num += 1
        return num
    return incrementer


def counter():
    num = 0

    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer


c = counter()
c()
c()
c()

x = "Hi"


def read_x():
    print(x)


read_x()

# ternary operator
# The ternary operator is used for inline conditional expressions

n = 5
" greater than 2 " if n > 2 else "smaller than or eaqual to 2"

# ternary operators can be nested

"hello" if n > 10 else "goodbye" if n > 3 else "good day"


st = "[1,2,3,4]"

lis = eval(st)

lis
type(lis)

st = "{1,2,3,4}"
eval(st)

st = "{1:'data',2:'input',3:'int',4:'out'}"
eval(st)

user_input = int(input("what is 2*2 : ?"))

while user_input != 4:
    user_input = input("the input is wrong please try one more time ")
    if user_input == 4:
        print("hurrah you got the output")
        break

# explanation for for loop

for outerloop in range(5):
    print('outerloop:', outerloop)
    for innerloop in range(5):
        print('innerloop:', innerloop)


# swapping the variables
# first way of swapping with temporary variable
a, b = 10, 20
c = a
a = b
b = c

print(a)
print(b)

# second way of swapping with out temporaray variable
a = 10
b = 20
a = a + b
a
b = a - b
b
a = a - b
a

print(a)
print(b)

# easiest way in python
a = 10
b = 20

a,  b = b, a
a
b

a, b = 2, 5

a = a ^ b
b = a ^ b
a = a ^ b

a, b


True == 1

False == 0

var = [3, 5, 0, 9]
var[False]
var[True]


def check_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("this is leap year")
    else:
        print("not leap year")


check_year(1956)

check_year(2012)

check_year(2019)

# check with calender module
import calendar

calendar.isleap(1956)


def check_year(year):
    if calendar.isleap(year) == True:
        print("this is leap year")
    else:
        print("not leap year")


check_year(2012)

s = "hello"
list(s)

des = '       hello     '
des.strip()
des.lstrip()
des.rstrip()

data = 'hello python'


l = []
for i in data:
    l.append(i)

print(l)


# inheriting python oops concept
class Base():
    def hi(self):
        return "hello"


class Child(Base):
    def hello(self):
        return 6


c = Child()
c.hello()
c.hi()


# printing stars
n = int(input("enter the value of n:,"))
for i in range(1, n + 1):
    print(i * '*')

for i in range(1, n + 1):
    print(" " * (n - i) + i * "*")

# class private variables gathering


class Foo():
    def __init__(self):
        self.__boo = 1  # private variables
        print('sel.__boo is', self.__boo)


f = Foo()
# f.__boo it returns attribute error

f._Foo__boo

# swapping program


class Hello():
    def setString(self, string):
        self.string = string

    def swap(self):
        return self.string[::-1]

    @property
    def swapPro(self):
        return self.string[::-1]


c = Hello()
c.setString('python learning')

c.swap()

c.swapPro


# python dont have pre /post increment

a = 2

print(++a)

print(+(+a))

a += 1

print(a)

a = a + 1

print(a)


def foo(var=5):
    var += 1.1
    return var


print(foo(), foo(1))


for j in range(1, 11):
    print([f"{j} odd", f"{j} even"][j % 2 == 0])

character = "Iron man"

movie = "Avengers end game"

print("will" + character + "live in a" + movie + "?")

print("will {} live in a {} ?".format(character, movie))
print("will %s live in a %s?" % (character, movie))
print("will {1} live in a{0}?".format(movie, character))
print(f"will {character} live in a{movie}")

# The chr() method returns a character whose unicode point is num, an integer
alpha = 65  # small letters starts from 97

for ind in range(7):
    for jnd in range(ind + 1):
        print(chr(alpha), end=" ")
    alpha += 1
    print()

name = "jeevan"
name.center(30)
name.ljust(25)
name.rjust(30)
name.ljust(25, '-')
name.rjust(30, '_')


try:
    1 + 2
except TypeError:
    print("exception is raised")

else:
    print("no exception is raised")

try:
    1 / 0
except ZeroDivisionError:
    print('dont divisible with zero')

else:
    print("no exception is raised")

x = 10
var_name = 10
a, b, c, d = 1, 2, 3, 4
a
b
c
d

a, *b = 1, 2, 3, 4, 5, 6
a
b

x = 10


def func(a, b=10, *args, **kwargs):
    print(a)
    print(b)
    print(*args)
    print(**kwargs)


func(1, 2, [3, 4, 5, 5], {1: "1", 2: "2"})

print("this is programming", end=',')

for i in [1,2,3,4,5]:
    print(i,end='@')

s =(1,2,3,4,5,6,[])
e=(1,2,3,4,())
d=([1,2,3],[4,5,6])
d.append(4)
s
d
s[6].insert(0,0)
s
