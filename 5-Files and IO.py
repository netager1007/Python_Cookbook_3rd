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
