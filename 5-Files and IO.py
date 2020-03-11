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

