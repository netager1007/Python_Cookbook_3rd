# CHAPTER 5: Files and I/O

# 5.1 Reading and Writing Text Data
# Problem
# You need to read or write text data, possibly in different text encodings such as ASCII,
# UTF-8, or UTF-16.`

# Solution
# Use the open() function with mode rt to read a text file. For example:

with open('test.txt', 'rt') as f:   # Read the entire file as a single string
    data = f.read()
    print('data:', data)

with open('test.txt', 'rt') as f:   # Iterate over the lines of the file
    for line in f:
        print('Line:', line, end='')
        # process line

# Similarly, to write a text file, use open() with mode wt to write a file, clearing and
# overwriting the previous contents (if any). For example:

text1 = 'LEE SOON CHEON'
text2 = 'SONG SU JIN'
with open('testw.txt', 'wt') as f:   # Write chunks of text data
    f.write(text1)
    f.write(text2)

line1 = 'LEE HYUN WOO'
line2 = 'LEE HYUN JOON'

with open('testw.txt', 'wt') as f:
    print(line1, file=f)
    print(line2, file=f)
print('')

# To append to the end of an existing file, use open() with mode at.
# By default, files are read/written using the system default text encoding, as can be found
# in sys.getdefaultencoding(). On most machines, this is set to utf-8. If you know
# that the text you are reading or writing is in a different encoding, supply the optional
# encoding parameter to open(). For example:
import sys
print(sys.getdefaultencoding())

with open('testw.txt', 'rt', encoding='latin-1') as f:
    data = f.read()
    print(data)


# When control leaves the
# with block, the file will be closed automatically. You don’t need to use the with statement,
# but if you don’t use it, make sure you remember to close the file:
f = open('test.txt', 'rt')
data = f.read()
f.close()         # You must close the file

# Another minor complication concerns the recognition of newlines, which are different
# on Unix and Windows (i.e., \n versus \r\n). By default, Python operates in what’s known
# as “universal newline” mode. In this mode, all common newline conventions are recognized,
# and newline characters are converted to a single \n character while reading.
# Similarly, the newline character \n is converted to the system default newline character
# on output. If you don’t want this translation, supply the newline='' argument to
# open(), like this:

with open('testw.txt', 'rt', newline='') as f:
    data = f.read()
    print(data)

# To illustrate the difference, here’s what you will see on a Unix machine if you read the
# contents of a Windows-encoded text file containing the raw data hello world!\r\n:

f = open('hello.txt', 'rt')  # Newline translation enabled (the default)
print(f.read())              # Return : 'hello world!\n'
f.close()

g = open('hello.txt', 'rt', newline='')  # Newline translation disable
print(g.read())                          # Return : 'hello world!\r\n'
g.close()

# A final issue concerns possible encoding errors in text files. When reading or writing a
# text file, you might encounter an encoding or decoding error. For instance:
f = open('test1.txt', 'rt', encoding='ascii')
try:
    f.read()
except UnicodeDecodeError as e:
    print(e)

# If encoding errors are still a possibility, you can supply an
# optional errors argument to open() to deal with the errors. Here are a few samples of
# common error handling schemes:

# Replace bad chars with Unicode U+fffd replacement char
with open('test1.txt', 'rt', encoding='ascii', errors='replace') as f:
    print(f.read())

with open('test1.txt', 'rt', encoding='ascii', errors='ignore') as g:
    print(g.read())

with open('test1.txt', 'rt', encoding='utf-8') as h:
    print(h.read())


# 5.2 Printing to a File
# Problem
# You want to redirect the output of the print() function to a file.

# Solution
# Use the file keyword argument to print(), like this:
with open('somefile.txt', 'wt') as f:
    print('Hello World!', file=f)

# 5.3 Printing with a Different Separator or Line Ending

# Problem
# You want to output data using print(), but you also want to change the separator
# character or line ending.

# Solution
# Use the sep and end keyword arguments to print() to change the output as you wish.
# For example:
print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')

# Use of the end argument is also how you suppress the output of newlines in output. For
# example:
for i in range(5):
    print(i)

for i in range(5):
    print(i, end=' ')
print('')
# Discussion
# Using print() with a different item separator is often the easiest way to output data
# when you need something other than a space separating the items. Sometimes you’ll
# see programmers using str.join() to accomplish the same thing. For example:

print(','.join(['ACME', '50', '91.5']))   # I don't know why error occered

row = ('ACME', 50, 91.5)
try:
    print(','.join(row))
except TypeError as e:
    print(e)

print(','.join(str(x) for x in row))  # To convert int to str


# 5.4 Reading and Writing Binary Data
# Problem
# You need to read or write binary data, such as that found in images, sound files, and so
# on.

# Solution
# Use the open() function with mode rb or wb to read or write binary data. For example:
with open('somefile.bin', 'wb') as f:    # Write binary data to a file
    f.write(b'Hello World')

with open('somefile.bin', 'rb') as f:    # Read the entire file as a single byte string
    data = f.read()
    print(data)
    print(type(data))

with open('somefile.bin', 'rt') as f:
    data = f.read()
    print(data)
    print(type(data))

# When reading binary, it is important to stress that all data returned will be in the form
# of byte strings, not text strings. Similarly, when writing, you must supply data in the
# form of objects that expose data as bytes (e.g., byte strings, bytearray objects, etc.).

# Discussion
# When reading binary data, the subtle semantic differences between byte strings and text
# strings pose a potential gotcha. In particular, be aware that indexing and iteration return
# integer byte values instead of byte strings. For example:

t = 'Hello World'   # Text string
print(t[0])
for c in t:
    print(c)

b = b'Hello World'
print(b[0])
for c in b:
    print(c)

# If you ever need to read or write text from a binary-mode file, make sure you remember
# to decode or encode it. For example:
with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')
print(text)

with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))

# A lesser-known aspect of binary I/O is that objects such as arrays and C structures can
# be used for writing without any kind of intermediate conversion to a bytes object. For
# example:
import array
nums = array.array('i',[1, 2, 3, 4])
print(nums)
with open('data.bin', 'wb') as f:
    f.write(nums)

# This applies to any object that implements the so-called “buffer interface,” which directly
# exposes an underlying memory buffer to operations that can work with it. Writing
# binary data is one such operation.
# Many objects also allow binary data to be directly read into their underlying memory
# using the readinto() method of files. For example:
import array
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb') as f:
    f.readinto(a)
print(a)


# 5.5 Writing to a File That Doesn't Already Exist

# Problem
# You want to write data to a file, but only if it doesn’t already exist on the filesystem.

# Solution
# This problem is easily solved by using the little-known x mode to open() instead of the
# usual w mode. For example:
with open('somefile', 'wt')as f:
    f.write('Hello\n')

try:
    with open('somefile', 'xt')as f:
        f.write('Hello\n')
except FileExistsError as e:
    print(e)

# Discussion
# This recipe illustrates an extremely elegant solution to a problem that sometimes arises
# when writing files (i.e., accidentally overwriting an existing file). An alternative solution
# is to first test for the file like this:
import os
if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write('Hello\n')
else:
    print('File already exists!')

# 5.6 Performing I/O Operations on a String

# Problem
# You want to feed a text or binary string to code that’s been written to operate on filelike
# objects instead.

# Solution
# Use the io.StringIO() and io.BytesIO() classes to create file-like objects that operate
# on string data. For example:
import io

s = io.StringIO()
s.write('Hello World\n')
print('This is a test', file=s)

print(s.getvalue())    # Get all of the data writtten so far

# Wrap a file interface around an existing string
s = io.StringIO('Hello\nWorld\n')
print(s.read(4))
print(s.read())
print(s.getvalue())

# The io.StringIO class should only be used for text. If you are operating with binary
# data, use the io.BytesIO class instead. For example:
s = io.BytesIO()
s.write(b'binary data')
for i in s.getvalue():
    print(i)
print(s.getvalue())

# Discussion
# The StringIO and BytesIO classes are most useful in scenarios where you need to mimic
# a normal file for some reason. For example, in unit tests, you might use StringIO to
# create a file-like object containing test data that’s fed into a function that would otherwise
# work with a normal file.
# Be aware that StringIO and BytesIO instances don’t have a proper integer filedescriptor.
# Thus, they do not work with code that requires the use of a real system-level
# file such as a file, pipe, or socket.

# 5.7 Reading and Writing Compressed Datafiles

# Problem
# You need to read or write data in a file with gzip or bz2 compression.

# Solution
# The gzip and bz2 modules make it easy to work with such files. Both modules provide
# an alternative implementation of open() that can be used for this purpose. For example,
# to read compressed files as text, do this:

# gzip compression
import gzip

# gzip compression
import gzip

with gzip.open('somefile.gz', 'wt') as f:
    f.write('abc')

with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

# bz2 compression
import bz2

with bz2.open('somefile.bz2', 'wt') as f:
    f.write('abc')

with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()


# Discussion
# For the most part, reading or writing compressed data is straightforward. However, be
# aware that choosing the correct file mode is critically important. If you don’t specify a
# mode, the default mode is binary, which will break programs that expect to receive text.
# Both gzip.open() and bz2.open() accept the same parameters as the built-in open()
# function, including encoding, errors, newline, and so forth.

# When writing compressed data, the compression level can be optionally specified using
# the compresslevel keyword argument. For example:
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write('abcdef')

# The default level is 9, which provides the highest level of compression. Lower levels offer
# better performance, but not as much compression.
# Finally, a little-known feature of gzip.open() and bz2.open() is that they can be layered
# on top of an existing file opened in binary mode. For example, this works:

import gzip
f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()
print(text)

import gzip
with open('somefile.gz', 'rb') as f:
    with gzip.open(f, 'rt') as g:
        text = g.read()
print(text)

# Discussion
# A little-known feature of the iter() function is that it can create an iterator if you pass
# it a callable and a sentinel value. The resulting iterator simply calls the supplied callable
# over and over again until it returns the sentinel, at which point iteration stops.
# In the solution, the functools.partial is used to create a callable that reads a fixed
# number of bytes from a file each time it’s called. The sentinel of b'' is what gets returned
# when a file is read but the end of file has been reached.
# Last, but not least, the solution shows the file being opened in binary mode. For reading
# fixed-sized records, this would probably be the most common case. For text files, reading
# line by line (the default iteration behavior) is more common.


# 5.9 Reading Binary Data into a Mutable Buffer

# Problem
# You want to read binary data directly into a mutable buffer without any intermediate
# copying. Perhaps you want to mutate the data in-place and write it back out to a file.

# Solution
# To read data into a mutable array, use the readinto() method of files. For example:
import os.path

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

# Write a sample file
with open('somefile.bin', 'wb') as f:
    f.write(b'Hello World')
buf = read_into_buffer('somefile.bin')
print(buf)
buf[0:5] = b'Hallo'
print(buf)

with open('newsample.bin', 'wb') as f:
    f.write(buf)

# Discussion
# The readinto() method of files can be used to fill any preallocated array with data. This
# even includes arrays created from the array module or libraries such as numpy. Unlike
# the normal read() method, readinto() fills the contents of an existing buffer rather
# than allocating new objects and returning them. Thus, you might be able to use it to
# avoid making extra memory allocations. For example, if you are reading a binary file
# consisting of equally sized records, you can write code like this:

record_size = 32       # Size of each record(adjust value)

buf = bytearray(record_size)
with open('somefile', 'rb') as f:
    while True:
        n = f.readinto(buf)    # Return : number of bytes actually read
        if n < record_size:
            break
        # Use the contents of file

# Another interesting feature to use here might be a memoryview, which lets you make
# zero-copy slices of an existing buffer and even change its contents. For example:
print(buf)
m1 = memoryview(buf)
m2 = m1[-5:]
print(m2)
print(m2[:])
print(buf)

# One caution with using f.readinto() is that you must always make sure to check its
# return code, which is the number of bytes actually read.
# If the number of bytes is smaller than the size of the supplied buffer, it might indicate
# truncated or corrupted data (e.g., if you were expecting an exact number of bytes to be
# read).
# Finally, be on the lookout for other “into” related functions in various library modules
# (e.g., recv_into(), pack_into(), etc.). Many other parts of Python have support for
# direct I/O or data access that can be used to fill or alter the contents of arrays and buffers.
# See Recipe 6.12 for a significantly more advanced example of interpreting binary structures
# and usage of memoryviews.


# 5.10 Memory Mapping Binary Files

# Problem
# You want to memory map a binary file into a mutable byte array, possibly for random
# access to its contents or to make in-place modifications.

# Solution
# Use the mmap module to memory map files. Here is a utility function that shows how to
# open a file and memory map it in a portable manner:

import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

# To use this function, you would need to have a file already created and filled with data.
# Here is an example of how you could initially create a file and expand it to a desired
# size:
size = 1000000
with open('data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

m = memory_map('data')
print(len(m))
print(m[0:10])
print(m[0])

m[0:11] = b'Hello World'       # Reassign a slice
print(m.closed)
m.close()

with open('data', 'rb') as f:  # Verify that changes were made
    print(f.read(11))


with memory_map('data') as m:
    print(len(m))
    print(m[0:10])
print(m.closed)

# By default, the memory_map() function shown opens a file for both reading and writing.
# Any modifications made to the data are copied back to the original file. If read-only
# access is needed instead, supply mmap.ACCESS_READ for the access argument. For
# example:
with memory_map('newsample.bin', mmap.ACCESS_READ) as m:
    print(len(m))
    print(m[0:11])

# Discussion
# Using mmap to map files into memory can be an efficient and elegant means for randomly
# accessing the contents of a file. For example, instead of opening a file and performing
# various combinations of seek(), read(), and write() calls, you can simply map the
# file and access the data using slicing operations.
# Normally, the memory exposed by mmap() looks like a bytearray object. However, you
# an interpret the data differently using a memoryview. For example:
m = memory_map('data')
v = memoryview(m).cast('I')
v[0] = 7
print(m[0:4])
m[0:4] = b'\x07\x01\x00\x00'
print(v[0])


# 5.11 Manipulating Pathnames
# Problem
# You need to manipulate pathnames in order to find the base filename, directory name,
# absolute path, and so on.

import os
path = '/User/JBB/Data/data.csv'
print(os.path.basename(path))   # Return 'data.csv' : Get the last component of the path
print(os.path.dirname(path))    # Get the directory name
print(os.path.join('tmp', 'data', os.path.basename(path))) # Join path components together
                                                           # Return : /tmp/data/data.csv
print(os.path.join('tmp', 'data', 'data.csv'))
path = '~/Data/data.csv'
print(os.path.expanduser(path))  # Expand the user's home directory
print(os.path.splitext(path))    # Split the file extension

# Discussion
# For any manipulation of filenames, you should use the os.path module instead of trying
# to cook up your own code using the standard string operations. In part, this is for
# portability. The os.path module knows about differences between Unix and Windows
# and can reliably deal with filenames such as Data/data.csv and Data\data.csv. Second,
# you really shouldn’t spend your time reinventing the wheel. It’s usually best to use the
# functionality that’s already provided for you.


# 5.12 Testing for the Existence of a File
import os
print(os.path.exists('test.txt'))
print(os.path.exists('/tmp/spam'))

print(os.path.isfile('test.txt'))  # Is a regular file
print(os.path.isdir('test.txt'))   # Is a directory
print(os.path.islink('test.txt'))   # Is a symbolic link
print(os.path.realpath('test.txt'))   # Get the file linked to

# If you need to get metadata (e.g., the file size or modification date), that is also available
# in the os.path module.
print(os.path.getsize('test.txt'))

print(os.path.getmtime('test.txt'))
import time
print(time.ctime(os.path.getmtime('test.txt')))



