# 1.1 Unpacking a Sequence into Separate Variables
p = (4, 5)
x, y = p
print(x)
print(y)

data = ['ACME', 50, 91.1, (2012,12,21)]
name, shares, price, date = data
print('name:', name, 'shares:', shares, 'price:', price, 'date:', date)

s = 'Hello'
a, b, c, d, e = s
print('a:', a, 'b:', b, 'c:', c, 'd:', d, 'e:', e)

# When unpacking, you may sometimes want to discard certain values.
data = ['ACME', 50, 91.1, (2012,12,21)]
_, shares, price, _ = data                 # discar name, date
print('shares:', shares, 'price:', price )


# 1.2 Unpacking Elements from Iterables of Arbitrary Length
# When unpacking, "too many values to unpack" exception
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_number = user_record
print('name:', name, 'email:', email, 'phone-number:', phone_number)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]

def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print('uname:', uname, 'homedir:', homedir, 'sh:', sh)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_,(*_, year) = record
print('name:', name, 'year:', year)

items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print('head:', head, 'tail:', tail)

#items = [1, 10, 7, 4, 5, 9]
#items = [1, 10]
items = [1]
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
print(sum(items))


# 1.3 Keepingthe Last N Items
from collections import deque
def search(lines, pattern, history=5):
    previous_line = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
# Example use on a file
#if __name__ == '__main__':
#    with open('somefile.txt') as f:
#        for line, prevlines in search(f, 'python', 5):
#            for pline in prevlines:
#                print(pline, end='')
#            print(line, end='')
#
        print('-'*20)

# About deque()
# Using deque(maxlen=N) creates a fixed-sized queue. When new items are added and
# the queue is full, the oldest item is automatically removed.
q = deque(maxlen=3)
q.append(1)
print(q)
q.append(2)
print(q)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)

q = deque()
q.append(1)
print(q)
q.append(2)
print(q)
q.append(3)
print(q)
q.appendleft(4)
print(q)
q.pop()
print(q)
q.popleft()
print(q)


# 1.4 Finding the Largest or Smallest N Items
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print('3 of Largest:', heapq.nlargest(3, nums))
print('3 of Smallest:', heapq.nsmallest(3, nums))

# nlargest(), nsmallest() also accept a key parameter that allows them to be used
# with more complicated data structures.
#TODO: I can't understand
portfolio = [
 {'name': 'IBM', 'shares': 100, 'price': 91.1},
 {'name': 'AAPL', 'shares': 50, 'price': 543.22},
 {'name': 'FB', 'shares': 200, 'price': 21.09},
 {'name': 'HPQ', 'shares': 35, 'price': 31.75},
 {'name': 'YHOO', 'shares': 45, 'price': 16.35},
 {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print('cheap:', cheap, '\nexpensive:', expensive)


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import heapq
heap = list(nums)
heapq.heapify(heap)
print('id(heap):', id(heap), 'id(nums):', id(nums), 'heap:', heap)

print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))


# 1.5 Implementing a Priority Queue
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue =[]
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
        print('[push()]:', self._queue)


    def pop(self):
        print('[pop()]:', self._queue)

        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.push(Item('lee'), 6)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

# Compare tuple
a = Item('foo')
b = Item('bar')
#print(a < b)    # Exception Error Occured

a = (1, Item('foo'))
b = (5, Item('bar'))
print(a < b)   # print Ture. If you make (priority, item) tuples, they can be compared
               # as long as the priorities are different.
c = (1, Item('grok'))
#print(a < c)   # Exception Error Occured

# (priority, index, item) tuples, you avoid this problem entirely since no two tuples
# will ever have the same valuefor index
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
print(a < b)
print(a < c)


# 1.6 Mapping Keys to Multiple Values in a Dictionary
d = {'a':[1, 2, 3],
     'b':[4, 5]
     }

e = {'a':{1, 2, 3},
     'b':{4, 5}
     }

# defaultdict() in the collections module
# A feature of defaultdict() is that it automatically initializes the first value
# so you can simply focus on adding items.
from collections import defaultdict
c = defaultdict(list)
c['a'].append(1)
c['a'].append(2)
c['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print('abc:', c, d)

e = {}
e.setdefault('a', []).append(1)
e.setdefault('a', []).append(2)
e.setdefault('b', []).append(4)
print(e)

# multivalued dictionary

d = {}
pairs = [('a', 1)]
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)


# OrderedDict from the collections module
# To control the order of items in a dictionary.
from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key, value in d.items():
    print(key, value, d[key])

# serialize data
import json
print(json.dumps(d))


# 1.8 Calculating with Dictionaries
prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print('min_price:', min_price, 'max_price:', max_price)
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))
#print(max(prices_and_names))  # ValueError : max() arg is an empty sequence

print('min(prices):', min(prices), 'max(prices):', max(prices))
print('min(prices.values()):', min(prices.values()), 'max(prices.values):', max(prices.values()))

#min(price, key=lambda k: price[k])
#min(prices, key='AAPL')
print(min(prices))
print(min(prices.keys()))
print(min(prices.values()))


prices = {'AAA':45.23, 'ZZZ': 45.23}
print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))


# 1.9 Finding Commonalities in Two Dictionaries
a = {
    'x':1,
    'y':2,
    'z':3
}

b = {
    'w':10,
    'x':11,
    'y':2
}

print(a, b)
print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())

c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)


# 1.10 Removing Duplicates from a Sequence while Maintaining Order
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))

#TODO: It's very diffcult. Study Again
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(set(a))


# 1.11 Naming a Slice
######### 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100          .......513.25     ..........'
cost = int(record[20:32]) * float(record[40:48])
print(cost)
SHARES = slice(20, 32)
PRICE = slice(40, 48)
print(SHARES, PRICE)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])
print(items[a])

items[a] = [10, 11]
print(items)
del items[a]
print(items)

a = slice(10, 50, 2)
print(a.start)
print(a.stop)
print(a.step)

s = 'HelloWorld'
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])


# 1. 12 Determining the Most Frequently Occurring Items in a Sequence
# Counter(), most_common()
words = [
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
 'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(word_counts)
print(top_three)

print(word_counts['not'])
print(word_counts['eyes'])

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1
print(word_counts['eyes'])
print(word_counts)

word_counts.update(morewords)
print(word_counts['eyes'])
print(word_counts)

a = Counter(words)
b = Counter(morewords)
print(a)
print(b)

c = a + b    # Combine Counter
print(c)

d = a - b    # Subtract counts
print(d)

# 1.13 Sorting a List of Dictionaries by a Common Key
rows = [
 {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
 {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
 {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
 {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
from operator import itemgetter, attrgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_uid)

# itemgetter() can also accept multiple keys.
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

rows_by_fname = sorted(rows, key=lambda r: r['fname'])
print(rows_by_fname)
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'],r['fname']))
print(rows_by_lfname)

print(sorted("This is at tost string from Andrew".split(), key=str.lower))

print('min itemgetter:', min(rows, key=itemgetter('uid')))
print('max itemgetter:', max(rows, key=itemgetter('uid')))


# 1.14 Sorting Objects Without Native Comparison Support
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
print(users)
print(sorted(users, key=attrgetter('user_id')))
print(sorted(users, key=lambda u: u.user_id))


# 1.15 Grouping Records Together Based on a Field : itertools.groupby()
from operator import itemgetter
from itertools import groupby

rows = [
 {'address': '5412 N CLARK', 'date': '07/01/2012'},
 {'address': '5148 N CLARK', 'date': '07/04/2012'},
 {'address': '5800 E 58TH', 'date': '07/02/2012'},
 {'address': '2122 N CLARK', 'date': '07/03/2012'},
 {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
 {'address': '1060 W ADDISON', 'date': '07/02/2012'},
 {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
 {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
]
print('Before: ', rows)
rows.sort(key=itemgetter('date'))  # Sort by the desired field first
print('After: ', rows)

# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('       ', i)

from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']:
    print(r)

print(rows_by_date)


# 1.16 Filtering Sequence Elements
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

pos = [n for n in mylist if n > 0]
print(pos)

pos = (n for n in mylist if n > 0)      # [] 와 ()의 차이
for x in pos:
    print(x)
print(pos)

# filter()
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math
print([math.sqrt(n) for n in mylist if n > 0])
print(list(math.sqrt(n) for n in mylist if n > 0))

clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)
clip_neg = [n if n < 0 else 0 for n in mylist]
print(clip_neg)

# itertools.compress()
addresses = [
 '5412 N CLARK',
 '5148 N CLARK',
 '5800 E 58TH',
 '2122 N CLARK'
 '5645 N RAVENSWOOD',
 '1060 W ADDISON',
 '4801 N BROADWAY',
 '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(addresses, more5)))


# 1.17 Extracting a Subset of a Dictionary
prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}

# Make a dictionary of all price over 200
p1 = {key:value for key, value in prices.items() if value > 200}
print(p1)

# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:value for key, value in prices.items() if key in tech_names}
print(p2)

# dict()
p1 = dict((key, value) for key, value in prices.items() if value > 200)
print(p1)

# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key:prices[key] for key in prices.keys() & tech_names}
print(p2)


# 1.8 Mapping Names to Sequence Elements

# collections.namedtuple()
from collections import namedtuple
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
print(Subscriber)
sub = Subscriber('jonesy@example.com','2012-10-19')
print(sub)
print(sub.addr, sub.joined)
print(len(sub))
addr, joined = sub
print(addr, joined)

#
from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

s = Stock('ACME', 100, 123.45)
print(s)
#s.shares = 75    # Error Occured. Why namedtuple is immutable
s._replace(shares=75)     # _replace()
print(s)
s = s._replace(shares=75) # namedtuple() 값 변경 방법
print(s)


from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

stock_prototype = Stock('', 0, 0.0, None, None)  # Create a prototype instance
def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
print(stock_prototype)
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))


# 1.19 Transforming and Reducing Data at the Same Time
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

# Determine if any .py files exist in a directory
import os
dirname = 'c:/'
files = os.listdir(dirname)
print(files)
print(type(files))
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))   # Output a tuple as CSV

# Data reduction across fields of a data structure
portfolio = [
 {'name':'GOOG', 'shares': 50},
 {'name':'YHOO', 'shares': 75},
 {'name':'AOL', 'shares': 20},
 {'name':'SCOX', 'shares': 65}
]
min_share = min(s['shares'] for s in portfolio)
print(min_share)

nums = [1, 2, 3, 4, 5]
s = sum((x * x for x in nums))    # Pass generator-expr as argument
print(s)
s = sum(x * x for x in nums)      # More elegnat syntax
print(s)
s = sum([x * x for x in nums])
print(s)

min_share = min(s['shares'] for s in portfolio)       # Original: Returns 20
print(min_share)
min_share = min(portfolio, key=lambda s: s['shares']) # Alternative: Returns {'name':'AOL', 'shares':20}
print(min_share)


# 1.20 Combining Multiple Mappings into a Single Mapping

# ChainMap Class
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap
c = ChainMap(a, b)
print(c['x'])         # Outputs 1 (from a)
print(c['y'])         # Outputs 2 (from b)
print(c['z'])         # Outputs 3 (from a)

print(len(c))
print(list(c.keys()))
print(list(c.values()))
c['z'] = 10
c['w'] = 40
print(a)
print(b)
print(c)
#del c['y']           # Error Occured

values = ChainMap()
values['x'] = 1
values['y'] = 11
values = values.new_child()  # Add a new mapping
values['x'] = 2
values['y'] = 22
values = values.new_child()  # Add a new mapping
values['x'] = 3
values['y'] = 4
print(values)
values = values.parents      # Discard last mapping
print(values)
values = values.parents      # Discard last mapping
print(values)
for key, value in values.items():
    print(key, value)
print(list((key, values[key]) for key in values.keys()))

# update() in dict()
a = {'x':1, 'z':3}
b = {'y':2, 'z':4}
merged = dict(b)
merged.update(a)
print('a: ', a)
print('b: ', b)
print(merged)
a['x'] = 13         # merged 에 영향을 주지 않음
print('a: ', a)
print('b: ', b)
print(merged)

# but ChainMap() is different result
a = {'x':1, 'z':3}
b = {'y':2, 'z':4}
merged = ChainMap(a, b)
print('a: ', a)
print('b: ', b)
print(merged)
a['x'] = 42        # a 와 ChainMap 둘다 변경 됨.
print('a: ', a)
print('b: ', b)
print(merged)

b['y'] = 22        # a 와 ChainMap 둘다 변경 됨.
print('a: ', a)
print('b: ', b)
print(merged)







