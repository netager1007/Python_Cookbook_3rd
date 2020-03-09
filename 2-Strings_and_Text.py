# 2.1 Splitting Strings on Any of Multiple Delimiters

line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
print(re.split(r'[;,\s]\s*', line))  # \s : white space

fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
values = fields[::2]
delimiters = fields[1::2]+['']
print('values: ', values)
print('delimiters: ', delimiters)

print(''.join(v+d for v, d in zip(values, delimiters)))

print(re.split(r'(?:,|;|\s)\s*', line))


# 2.2 Matching Text at the Start or End of a String

# str.startswith() or str.endswith()
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
print(filename.startswith('sp'))
url = 'http://www.python.org'
print(url.startswith('http:'))

import os
filenames = os.listdir('.')
print(filenames)
print([name for name in filenames if name.endswith(('.c', '.h', '.py'))])
print(any(name.endswith('.py') for name in filenames))

from urllib.request import urlopen
def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(anme).read()
    else:
        with open(name) as f:
            return f.read()

choices = ['http:', 'ftp:']
url = 'http://www.python.org'
url.startswith(tuple(choices))               # startswith() 와 endswith() 함수는 str or tuple로 넘겨야 함

filename = 'spam.txt'
print(filename[-4:] == '.txt')
url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https' or url[:4] == 'ftp:')

import re
url = 'http://www.python.org'
print(re.match('http:|https:|ftp:', url))

# Useful endswith()
import os
dirname = '.'
if any(name.endswith(('.c', '.h')) for name in os.listdir(dirname)):
    print(name)
else:
    print('No File exists')


# 2.3 Matching Strings Using Shell Wildcard Patterns
# fnmatch() and fnmatchcase()
from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '*.TXT'))   # fnmatch()는 대소문자 구분하지 않음
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])

print(fnmatchcase('foo.txt', '*.TXT')) # fnmatchcase() 대소문자 구분

addresses = [
 '5412 N CLARK ST',
 '1060 W ADDISON ST',
 '1039 W GRANVILLE AVE',
 '2122 N CLARK ST',
 '4802 N BROADWAY',
]
from fnmatch import fnmatchcase
print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])

# 2.4 Matching and Searching for Text Patterns
text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah')           # Exact match
print(text.startswith('yeah'))  # Match at start or end
print(text.endswith('no'))      # Match at start or end
print(text.find('no'))          # Search for the location of the first occurrence
print(text.find('lee'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

# Precompile the regular expression pattern
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

# Capture groups by enclosing parts of the pattern in parentheses.
# Capture groups often simplify subsequent processing of the matched text.
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m)
print(m[0], m[1], m[2], m[3], m.groups())
month, day, year = m.groups()
print(month, day, year)


text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))   # Find all matches (notice splitting into tuples)
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

# findall() method searches the text and finds all matches, retruning them as a list.
# If you want to find matches iteratively, use the finditer() method instead.
for m in datepat.finditer(text):
    print(m.groups())

datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(datepat.match('11/27/2012abcdef'))
print(datepat.match('11/27/2012'))

# Simple text matching/searching operation, you can often skip the compilation step.
print(re.findall(r'(\d+)/(\d+)/(\d+)', text))

# 2.5 Searching and Replacing Text
# str.replace()
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))
print(text)                        # No change origin text

# re.sub()
# In second argument, backslashed digits such as \3 refer to capture group number
# in the pattern.
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

import re
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))

# For more complicated substitutions
from calendar import month_abbr
import re

#TODO: Dont' understand
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
def change_date(m):
    print(type(m))
    print(m)
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

print(datepat.sub(change_date, text))

# How many substitutions were made in addition to getting the replacement text,
# use re.subn() instead.
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
newtext, n = datepat.subn(r'\3-\2-/2', text)
print('n: ', n, 'newtext: ', newtext)


# 2.6 Searching and Replacing Case-Insensitive Text

# use re module and re.IGNORECASE flag
text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text))
print(re.findall('python', text, flags=re.IGNORECASE))
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))

#TODO: It's very difficult ~ Where is m from?
def matchcase(word):
    def replace(m):
        print('type(m): ', type(m))
        text = m.group()
        print('replace.text: ', text)
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))


# 2.7 Specifying a Regular Expression for the Shortest Match

# TODO: It's very difficult
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))

str_pat = re.compile(r'\"(.*?)\"')
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))


# 2.8 Writing a Regular Expression for Multiline Patterns

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
              multiline comment */'''
print(comment.findall(text1))
print(comment.findall(text2))   # When multiline, can't find

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

# Use re.DOTALL flag
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))


# 2.9 Normalizing Unicode Text to a Standard Representation

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1)
print(s2)
print(s1 == s2)
print('len(s1): ', len(s1), 'len(s2): ', len(s2))

import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(ascii(t1))
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)
print(ascii(t3))

s = '\ufb01'
print(s)
print(unicodedata.normalize('NFD', s))
print(unicodedata.normalize('NFKD', s))
print(unicodedata.normalize('NFKC', s))

s1 = 'Spicy Jalape\u00f1o'
t1 = unicodedata.normalize('NFD', s1)
print(t1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))


# 2.10 Working with Unicode Characters in Regular Expression
import re
num = re.compile('\d+')
m = num.match('123')    # ASCII digits
print(m.group())

print(num.match('\u0661\u0662\u0663'))
m1 = num.match('\u0661\u0662\u0663')
print(m1.group())

arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
s1 = pat.match(s)
print(s1.group())
pat.match(s.upper())
print(s.upper())


# 2.11 Stripping Unwanted Characters from Strings
# strip()

# Whitespace stripping
s = '          hello world  \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

t = '------hello====='
print(t.lstrip('-'))
print(t.strip('-='))

s = '   hello      world    \n'
s = s.strip()
print(s)

print(s.replace(' ',''))

import re
a = re.sub('\s+', ' ', s)
print('a: ', ascii(a))

# Reading lines of data from a file
data = 'abcd efg HIJ   KLMN   OPqrs'
fout = open('test.txt', 'wt')
fout.write(data)
fout.close()

with open('test.txt') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)


# 2.12 Sanitizing and Cleaning Up Text
# str.translate()
s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)
remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None    # Deleted
}

a = s.translate(remap)
print(a)

# Remove all combining characters
# A dictionary mapping every Unicode combining character to None is created
# using the dict.fromkeys()
#TODO : It is very difficult
import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))
print(cmb_chrs)
b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))
print(a.translate(cmb_chrs))

# Translation table that maps all Unicode decimal digit characters to their equivalent in ASCII
digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd'}
print(len(digitmap))

x = '\u0661\u0662\u0663'
print(x.translate(digitmap))


a = 'pýtĥöñ\fis\tawesome\r\n'
b = unicodedata.normalize('NFD', a)
c = b.encode('ascii', 'ignore').decode('ascii')
print(a)
print(b)
print(c)

# 2.13 Aligning Text Strings
# ljust(), rjust(), center()
text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
print(text.rjust(20, '='))
print(text.center(20, '*'))

print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
print(format(text, '=>20'))
print(format(text, '-<20'))
print(format(text, '*^20'))

print('{:>10s} {:>10s}'.format('Hello', 'World'))
x = 1.2345
print(format(x, '>10'))
print(format(x, '*^10'))

# 2.14 Combining and Concatenating Strings
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(''.join(parts))
print(','.join(parts))

a = 'Is Chicago'
b = 'Not Chicago?'
print(a + ' ' + b)
print('{} {}'.format(a, b))

a = 'Hello' 'world'
print(a)

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
s = ''
for p in parts:
    s += p
print(s)

data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

print(a + ':' + ':' +c)    # ugly
print(':'.join([a, b, c])) # Still ugly
print(a, b, c, sep=':')    # Better

# TODO: don't know
'''
source = 'abcd efgh hijklmn'
def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
        yield ''.join(parts)

f = open('combin.txt', 'wt')
for part in combine(sample(), 32768):
    f.write(part)
f.close()
'''


# 2.15 Interplating Variables in Strings
s = '{name} has {n} message.'
print(s.format(name='Guido', n=37))

# format_map() and vars()
name = 'Guido'
n = 37
print(s.format_map(vars()))

# Work with instances
class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n
a = Info('Guido', 37)
print(s.format_map(vars(a)))


# They do not deal gracefully with missing values.
try:
    s.format(name='Guido')  # Error Occure
except KeyError as e:
    print('Error: ', e)

# Way to avoid this is to define an alternative dictionary class
# with a __missing__() method.
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n   # Make sure n is undefined
print(s.format_map(safesub(vars())))

# frame hack
import sys
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))

# 2.16 Reformating Text to a Fixed Number of Columns
# textwrap module
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
import textwrap
print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent='    '))
print(textwrap.fill(s, 40, subsequent_indent='    '))

# os.get_terminal_size()
#import os
#os.get_terminal_size()   # Error Occured


# 2.17 Handling HTML and XML Entities in Text
# html.escape()
s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))
print(html.escape(s, quote=False))   # Disable escaping of quotes

s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))
print(s)

s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
import html
p = HTMLParser()
print(html.unescape(s))

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))


# 2.18 Tokenizing Text
text = 'foo = 23 + 42 * 10'

tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

'''
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

scanner = master_pat.scanner('foo = 42')
print(scanner.match())
print(_.lastgroup, _.group())
'''

from collections import namedtuple

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
Token = namedtuple('Token', ['type', 'value'])
def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

tokens = (tok for tok in generate_tokens(master_pat, text)
          if tok.type != 'WS')
for tok in tokens:
    print(tok)

# TODO: Skip, because i can't understand
# 2.19 Writing a Simple Recursive Descent Parser


# 2.20 Performing Text Operations on Byte Strings
# Perform common text operations(stripping, searching, replacement) on byte strings.
data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

# In Byte arrays
data = bytearray(b'Hello World')
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))


data = b'FOO:BAR,SPAM'
import re
# re.split('[:,]', data)    # Error Occured
print(re.split(b'[:,]', data))

a = 'Hello World'    # Text string
print(a[0])
print(a[1])

b = b'Hello World'   # Byte string
print(b[0])
print(b[1])

s = b'Hello World'
print(s)
print(s.decode('ascii'))

print(b'%10s %10d %10.2f' % (b'ACME', 100, 490.1))
# print(b'{} {} {}'.format(b'ACME', 100, 490.1)) # Error Occured

print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))

# Write a UTF-8 filename
with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy')

# Get a directory listing
import os
print(os.listdir('.'))        # Text string (names are decoded)
print(os.listdir(b'.'))       # Byte string (names left as bytes)



