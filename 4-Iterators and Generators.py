# 4.1 Manually Consuming an Iterator
# You need to process items in an iterable, but for whatever reason, you can't
# or don't want to use a for loop.

# Normally, StopIteration is used to signal the end of iteration.
with open('test.txt') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        print('\nexcept[StopIteration]')
        pass

with open('test.txt') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')

print('')
items = [1, 2, 3]
it = iter(items)   # Get the iterator, Invokes items.__iter__()
print(next(it))    # Run the iterator, Invokes it.__next__()
print(next(it))
print(next(it))
try:
    print(next(it))
except StopIteration:
    pass


# 4.2 Delegating Iteration
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)

    for ch in root:
        print(ch)


# 4.3 Creating New Iteration Patterns with Generators
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for n in frange(0, 4, 0.5):
    print(n)
print(list(frange(0, 1, 0.125)))

def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

c = countdown(3)
print(c)
print(next(c))
print(next(c))
print(next(c))
try:
    print(next(c))
except StopIteration:
    pass

for num in c:
    print(num)


# 4.4 Implementing the Iterator Protocol
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()     # TODO : It's very difficult

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child1.add_child(Node(5))

    for ch in root.depth_first():
        print(ch)

# Python’s iterator protocol requires __iter__() to return a special iterator object that
# implements a __next__() operation and uses a StopIteration exception to signal
# completion. However, implementing such objects can often be a messy affair. For example,
# the following code shows an alternative implementation of the depth_first()
# method using an associated iterator class:

# TODO: You must review this example later
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, other_node):
        self._children.append(other_node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)

class DepthFirstIterator(object):
    ''' Depth-first traversal '''
    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        # Return myself if just started; create an iterator for children
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node

        # If processing a child, return its next item
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)
         # Advance to the next child and start its iteration
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)


# 4.5 Iterating in Reverse
# reversed() function
a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)

# Print a file backwards
# Be aware that turning an iterable into a list as shown could consume a lot of memory
# if it’s large.
f = open('test.txt')
for line in reversed(list(f)):
    print(line, end='')

# Many programmers don’t realize that reversed iteration can be customized on userdefined
# classes if they implement the __reversed__() method. For example:

# Defining a reversed iterator makes the code much more efficient, as it’s no longer necessary
# to pull the data into a list and iterate in reverse on the list.

# TODO: Can't execute
class Countdown:
    def __init__(self, start):
        self.start = start

        # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

print('')
c = Countdown(10)
for x in c:
    print(x)
print('')
for x in reversed(c):
    print(x)


# 4.6 Defining Generator Functions with Extra State
# Problem
# You would like to define a generator function, but it involves extra state that you would
# like to expose to the user somehow.

# Solution
# If you want a generator to expose extra state to the user, don’t forget that you can easily
# implement it as a class, putting the generator function code in the __iter__() method.
# For example:
from collections import deque

class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)
        print('linehistory.__init__')

    def __iter__(self):
        print('linehistory.__itter__')
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            print('[abc]', line)
            yield line

    def clear(self):
        self.history.clear()

# To use this class, you would treat it like a normal generator function. However, since it
# creates an instance, you can access internal attributes, such as the history attribute or
# the clear() method. For example:
with open('test.txt') as f:
    lines = linehistory(f)
    print('abcdef')
    for line in lines:
        print('for loop')
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')
    lines.clear()


f = open('test.txt')
lines = linehistory(f)
try:
    next(lines)
except TypeError as e:
    print(e)

f = open('test.txt')
lines = linehistory(f)
it = iter(lines)
print(next(it))
print(next(it))


# 4.7 Taking a Slice of an Iterator
# Problem
# You want to take a slice of data produced by an iterator, but the normal slicing operator
# doesn’t work

# Solution
# The itertools.islice() function is perfectly suited for taking slices of iterators and
# generators. For example:
def count(n):
     while True:
         yield n
         n += 1
c = count(0)

try:
    print(c[10:20])
except TypeError as e:
    print('Error Occured:', e)

# Now using islice()
import itertools
for x in itertools.islice(c, 10, 20):
    print(x)


# 4.8 Skipping the First Part of an Iterable
# Problem
# You want to iterate over items in an iterable, but the first few items aren’t of interest and
# you just want to discard them.

# Solution
# The itertools module has a few functions that can be used to address this task. The
# first is the itertools.dropwhile() function. To use it, you supply a function and an
# iterable. The returned iterator discards the first items in the sequence as long as the
# supplied function returns True. Afterward, the entirety of the sequence is produced.
# To illustrate, suppose you are reading a file that starts with a series of comment lines.
# For example:
with open('passwd.txt') as f:
    for line in f:
        print(line, end='')

print('')
print('')

from itertools import dropwhile
with open('passwd.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

print('')
print('')
from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)


# Discussion
# The dropwhile() and islice() functions are mainly convenience functions that you
# can use to avoid writing rather messy code such as this:
with open('passwd.txt') as f:
    # Skip over initial comments
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break
    # Process remaining lines
    while line:
        # Replace with useful processing
        print(line, end='')
        line = next(f, None)

# Discarding the first part of an iterable is also slightly different than simply filtering all
# of it. For example, the first part of this recipe might be rewritten as follows:
print('')
print('')
with open('passwd.txt') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line,end='')

# 4.9 Iterating Over All Possible Combinations or Permutations
# Problem
# You want to iterate over all of the possible combinations or permutations of a collection
# of items.

# Solution
# The itertools module provides three functions for this task. The first of these—iter
# tools.permutations()—takes a collection of items and produces a sequence of tuples
# that rearranges all of the items into all possible permutations (i.e., it shuffles them into
# all possible configurations). For example:
print('')
from itertools import permutations

items = ['a', 'b', 'c']
for p in permutations(items):
    print(p)

for p in permutations(items, 2):
    print(p)

# Use itertools.combinations() to produce a sequence of combinations of items taken
# from the input. For example:
print('')
from itertools import combinations

items = ['a', 'b', 'c']
for c in combinations(items, 3):
    print(c)
print('')
for c in combinations(items, 2):
    print(c)

print('')
for c in combinations(items, 1):
    print(c)

# itertools.combinations_with_replacement()
from itertools import combinations_with_replacement

for c in combinations_with_replacement(items, 3):
    print(c)


# 4.10 Iterating over the Index-Value Pairs of a Sequence
# Problem
# You want to iterate over a sequence, but would like to keep track of which element of
# the sequence is currently being processed.

# Solution
# The built-in enumerate() function handles this quite nicely:
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

print('')
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list, 1):
    print(idx, val)

def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
#            print('fields:', fields)
            try:
                count = len(fields[0])
            except ValueError as e:
                print('Line {}: Parse error: {} fields[0]: {}'.format(lineno, e, count))

parse_data('passwd.txt')


# enumerate() can be handy for keeping track of the offset into a list for occurrences of
# certain values, for example. So, if you want to map words in a file to the lines in which
# they occur, it can easily be accomplished using enumerate() to map each word to the
# line offset in the file where it was found:

# TODO: Review later
from collections import defaultdict
word_summary = defaultdict(list)

with open('passwd.txt', 'r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

print(word_summary)

# enumerate() is a nice shortcut for situations where you might be inclined to keep your
# own counter variable. You could write code like this:
# lineno = 1
# for line in f:
# Process line
# ...
#    lineno += 1

# But it’s usually much more elegant (and less error prone) to use enumerate() instead:
# for lineno, line in enumerate(f):
# Process line
# ...


data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]

# Correct!
for n, (x, y) in enumerate(data):
    print(n, (x, y))

# Error!
# for n, x, y in enumerate(data):


# 4.11 Iterating Over Multiple Sequences Simulataneously

# Problem
# You want to iterate over the items contained in more than one sequence at a time.

# Solution
# To iterate over more than one sequence simultaneously, use the zip() function. For
# example:
print('')

xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]

for x in zip(xpts, ypts):
    print(x)

print('')
for x, y in zip(xpts, ypts):
    print(x, y)

a = [1, 2, 3]              # 3 items
b = ['w', 'x', 'y', 'z']   # 4 items
for i in zip(a,b):
    print(i)               # 3 Results

# itertools.zip_longest() : 가장 긴 items 까지 출력
print('')
from itertools import zip_longest
for i in zip_longest(a, b):
    print(i)

for i in zip_longest(a, b, fillvalue=0):
    print(i)

# Discussion
# zip() is commonly used whenever you need to pair data together. For example, suppose
# you have a list of column headers and column values like this:

headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]

# Using zip(), you can pair the values together to make a dictionary like this:
s = dict(zip(headers, values))
print(s)

# Alternatively, if you are trying to produce output, you can write code like this:
for name, val in zip(headers, values):
    print(name, '=', val)

# It’s less common, but zip() can be passed more than two sequences as input. For this
# case, the resulting tuples have the same number of items in them as the number of input
# sequences. For example:
a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']

for i in zip(a, b, c):
    print(i)

# Last, but not least, it’s important to emphasize that zip() creates an iterator as a result.
# If you need the paired values stored in a list, use the list() function. For example:
print(zip(a, b))          # Result : <zip object at 0x1007001b8>
print(list(zip(a, b)))    # Result : [(1, 10), (2, 11), (3, 12)]


# 4.12 Iterating on Items in Separate Containers

# Problem
# You need to perform the same operation on many objects, but the objects are contained
# in different containers, and you’d like to avoid nested loops without losing the readability
# of your code.

# Solution
# The itertools.chain() method can be used to simplify this task. It takes a list of
# iterables as input, and returns an iterator that effectively masks the fact that you’re really
# acting on multiple containers. To illustrate, consider this example:

from itertools import chain
a = [1, 2, 3, 4]
b = ['x', 'y', 'z']

for x in chain(a, b):
    print(x)

# A common use of chain() is in programs where you would like to perform certain
# operations on all of the items at once but the items are pooled into different working
# sets. For example:

# Various working sets of items
active_items = set()
inactive_items = set()

# Iterate over all items
for item in chain(active_items, inactive_items):
    # process item
    pass

# This solution is much more elegant than using two separate loops, as in the following:

# for item in active_items:
#     Process item

# for item in inactive_items:
#     Process item

# Better : for x in chain(a, b):     Inefficent : for x in a + b


# 4.13 Creating Data Processing Pipelines

# Problem
# You want to process data iteratively in the style of a data processing pipeline (similar to
# Unix pipes). For instance, you have a huge amount of data that needs to be processed,
# but it can’t fit entirely into memory.

# Solution
# Generator functions are a good way to implement processing pipelines. To illustrate,
# suppose you have a huge directory of log files that you want to process:
# foo/
# access-log-012007.gz
# access-log-022007.gz
# access-log-032007.gz
# ...
# access-log-012008
# bar/
# access-log-092007.bz2
# ...
# access-log-022008
# Suppose each file contains lines of data like this:
# 124.115.6.12 - - [10/Jul/2012:00:18:50 -0500] "GET /robots.txt ..." 200 71
# 210.212.209.67 - - [10/Jul/2012:00:18:51 -0500] "GET /ply/ ..." 200 11875
# 210.212.209.67 - - [10/Jul/2012:00:18:51 -0500] "GET /favicon.ico ..." 404 369

# To process these files, you could define a collection of small generator functions that
# perform specific self-contained tasks. For example:

import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat, top):
    '''
    Find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path,name)

def gen_opener(filenames):
    '''
    Open a sequence of filenames one at a time producing a file object.
    The file is closed immediately when proceeding to the next iteration.
    '''
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()

def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators together into a single sequence.
    '''
    for it in iterators:
        yield from it
#        yield it

def gen_grep(pattern, lines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

# You can now easily stack these functions together to make a processing pipeline. For
# example, to find all log lines that contain the word python, you would just do this:
lognames = gen_find('*.txt', '.')
files = gen_opener(lognames)

#for i in files:
#    print(i)

lines = gen_concatenate(files)

print('lines:', lines)
#for i in lines:
#    print('i:', i)

pylines = gen_grep('(?i)python', lines)

for line in pylines:
    print(line)

# If you want to extend the pipeline further, you can even feed the data in generator
# expressions. For example, this version finds the number of bytes transferred and sums
# the total:
#lognames = gen_find('access-log*', 'www')
lognames = gen_find('*.txt', '.')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
bytecolumn = (line.rsplit(None, 1)[1] for line in pylines)

try:
    pass
#    bytes = (int(x) for x in bytecolumn if x != '-')
except ValueError as e:
    pass

#print('Total', sum(bytes))


# 4.14 Flattening a Nested Sequence

# Problem
# You have a nested sequence that you want to flatten into a single list of values.

# Solution
# This is easily solved by writing a recursive generator function involving a yield from
# statement. For example:

from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print(x)

items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    print(x)


# Discussion
# The yield from statement is a nice shortcut to use if you ever want to write generators
# that call other generators as subroutines. If you don’t use it, you need to write code that
# uses an extra for loop. For example:
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten(x):
                yield i
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flatten(items):
    print('new:', x)

items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    print('new1:', x)


# 4.15 Iterating in Sorted Order Over Merged Sorted Iterables

# Problem
# You have a collection of sorted sequences and you want to iterate over a sorted sequence
# of them all merged together.

# Solution
# The heapq.merge() function does exactly what you want. For example:
import heapq
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):
    print(c)

# It’s important to emphasize that heapq.merge() requires that all of the input sequences
# already be sorted.
import heapq
with open('test.txt', 'rt') as file1,      \
     open('passwd.txt', 'rt') as file2,    \
     open('merge_file.txt', 'wt') as outf:
     for line in heapq.merge(file1, file2):
         outf.write(line)


# 4.16 Replacing Infinite while Loops with an Iterator
# Problem
# You have code that uses a while loop to iteratively process data because it involves a
# function or some kind of unusual test condition that doesn’t fall into the usual iteration
# pattern.

# Solution
# A somewhat common scenario in programs involving I/O is to write code like this:

CHUNKSIZE = 9182

def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)

# Such code can often be replaced using iter(), as follows:
def reader(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        process_data(data)

# If you’re a bit skeptical that it might work, you can try a similar example involving files.
# For example:
print('TEST .....')
import sys
f = open('test.txt')
for chunk in iter(lambda: f.read(10), ''):
    print('[chunk] :', chunk)
    print('')
    n = sys.stdout.write(chunk)
    print('')

