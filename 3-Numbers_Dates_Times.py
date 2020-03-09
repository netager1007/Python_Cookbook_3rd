# 3.1 Numbers, Dates, and Times

print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.23, 1))
print(round(-1.27, 1))
print(round(1.25361, 3))
print(round(1.25, 1))
print(round(1.37, 1))
print(round(1.5))
print(round(2.5))

a = 1627731
print(round(a, -1))   # 1627730
print(round(a, -2))   # 1627700
print(round(a, -3))   # 1628000

x = 1.23456
print(format(x, '0.2f'))
print(format(x, '0.3f'))
print('value is {:0.3f}'.format(x))

a = 2.1
b = 4.2
c = a + b
print(c)

c = round(c, 2)     # "Fix" result (???)
print(c)


# 3.2 Performing Accurte Decimal Calculations

a = 4.2
b = 2.1
print(a + b)
print ((a + b) == 6.3)   # False : 부동소수점 계산의 함정

# Avoid such errors if you write your code using float instances.
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a+b)
print((a+b) == Decimal('6.3'))

from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print('a/b = ', a/b)

with localcontext() as ctx:
    ctx.prec = 3
    print('a/b = ', a/b)

with localcontext() as ctx:
    ctx.prec = 50
    print('a/b= ', a/b)

nums = [1.23e+18, 1, -1.23e+18]   # Notice how 1 disappears
print('sum(nums)= ', sum(nums))

import math
print('math.fsum(nums)= ', math.fsum(nums))


# 3.3 Formatting Numbers for Output
x = 1234.56789
print(format(x, '0.2f'))
print(format(x, '>10.1f'))
print(format(x, '<10.1f'))
print(format(x, '^10.1f'))
print(format(x, '0,.1f'))    # Inclusion of thousands separator
print(format(x, 'e'))        # 지수 표현, Used for exponential specifier
print(format(x, '0.2E'))     # 지수 표현, Used for exponential specifier


# General form of the width and precision : '[<>^]?width[,]?(.digits)?'
print('The value is {:0,.2f}'.format(x))
print('The value is {}'.format(x,'0,.2f'))  # different result

x = 1234.56789
print(format(x, '0.1f'))
print(format(-x, '0.1f'))

# translate()
swap_separators = { ord('.'):',', ord(','):'.' }
print(format(x, ',').translate(swap_separators))


# 3.4 Working with Binary, Octal, and Hexadecimal Integers
# bin(), oct(), hex()
x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

print(format(x, 'b'))   # if you don't want the 0b, 0o, 0x prefixes to appear.
print(format(x, 'o'))
print(format(x, 'x'))

x = -1234
print(format(x, 'b'))
print(format(x, 'x'))

x = -1234
print(format(2**32+x, 'b'))
print(format(2**32+x, 'x'))

print(int('4d2', 16))             # 16진수를 10진수로
print(int('10011010010', 2))      # 2진수를 10진수로

# import os
# os.chmod('script.py', 0755)   # Error Occured : invalid token
# os.chmod('script.py', 0o755)  # It's OK


# 3.5 Packing and Unpacking Large Intgers from Bytes
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
print(int.from_bytes(data, 'little'))
print(int.from_bytes(data, 'big'))

x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

# TODO : I can't understood
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
import struct
hi, lo = struct.unpack('>QQ', data)
print((hi << 64) + lo)

x = 0x01020304
print(x.to_bytes(4, 'big'))      # Big Edian
print(x.to_bytes(4, 'little'))   # Little Edian

x = 523 ** 23
print(x)
try:
    x.to_bytes(16, 'little')
except OverflowError as e:
    print("Error Occured: ", e)

print(x.bit_length())
nbytes, rem = divmod(x.bit_length(), 8)
if rem:
    nbytes += 1

print(x.to_bytes(nbytes, 'little'))


# 3.6 Performing Complex-Valued Math
# complex(real, imag)
a = complex(2, 4)       # 2 + 4j  : 복소수
b = 3 - 5j
print('a.real= ', a.real, 'a.imag= ', a.imag)
print('a.conjugate()= ', a.conjugate())

print('a+b= ', a+b)
print('a*b= ', a*b)
print('a/b= ', a/b)
print('abs(a)= ', abs(a))

import cmath
print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))

import numpy as np
a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(a)
print(a+2)
print(np.sin(a))

import math
try:
    math.sqrt(-1)
except ValueError as e:
    print('Error Occured: ', e)

import cmath
print(cmath.sqrt(-1))


# 3.7 Working with Infinity and NaNs
a = float('inf')
b = float('-inf')
c = float('nan')
print(a, b, c)

# math.isinf(), math.isnan()
print(math.isinf(a))
print(math.isinf(b))
print(math.isnan(c))

a = float('inf')
print(a+45)
print(a*10)
print(10/a)

a = float('inf')
print(a/a)
b = float('-inf')
print(a+b)

c = float('nan')
print(c+23)
print(c/2)
print(c*2)
print(math.sqrt(c))

c = float('nan')
d = float('nan')
print(c==d)
print(c is d)


# 3.8 Calculating with Fractions(분수)
# fractions module
from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a+b)      # 5/4 + 7/16
print(a*b)      # 5/4 * 7/16

c = a * b         # Getting numerator(분자)/denominator(분모)
print(c.numerator)
print(c.denominator)
print(float(c))   # Converting to a float
print(c.limit_denominator(8)) # Limiting the denominator of a value

x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)


# 3.9 Calculating with Large Numerical Arrays
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x*2)       # List의 곱은 문자열처럼 동작
try:
    print(x+10)
except TypeError as e:
    print('Error Occured: ', e)
print(x+y)       # 문자열 처럼 동작: 리스트의 item이 뒤에 붙음.

import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax*2)
print(ax+10)
print(ax+ay)
print(ax*ay)

def f(x):
    return 3*x**2 - 2*x + 7
print(f(ax))

print(np.sqrt(ax))
print(np.cos(ax))

grid = np.zeros(shape=(10000,10000), dtype=float)
print(grid)
grid += 10
print(grid)
print(np.sin(grid))

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[1])
print(a[:,1])
print(a[1:3, 1:3])
print(a[1:3, 1:3]+10)
print(a)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a+[100, 101, 102, 103])
print('')
print(a)
print(np.where(a<10, a, 10))


# 3.10 Performing Matrix(행렬) and Linear Algebra(선형대수학) Calculations
import numpy as np
m = np.array([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)
print(m.T)     # Transpose
#print(m.I)     # Inverse    Error Occured
v = np.array([[2], [3], [4]])
print(m)
print(v)
print(m*v)   # 단순 multiply
print(m@v)   # Dot Product

import numpy.linalg
print(numpy.linalg.det(m))  # Determinant
print(numpy.linalg.eigvals(m))  # Eigenvalues(고윳값, 고유치)

print(m)
print(v)
x = numpy.linalg.solve(m, v)
print(x)
print(m@x)


# 3.11 Picking Things at Random
import random
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))

# random.sample() : To take a sampling of N items
print(random.sample(values, 2))
print(random.sample(values, 2))
print(random.sample(values, 3))
print(random.sample(values, 3))

# random.shuffle()
print(values)
random.shuffle(values)
print(values)
random.shuffle(values)
print(values)

# randint()
print(random.randint(0, 10))  # 0 ~ 10 random number
print(random.randint(0, 10))

# random.random(): range 0 ~ 1, uniform floating-point values
print(random.random())
print(random.random())
print(random.random())

# random.getrandbits(): To get N random-bits expressed as an integer,
print(random.getrandbits(200))

# random module computs randdom number using the Mersenne Twister algorithm.
# You can alter the initial seed by using the random.seed()
random.seed()             # Seed based on system time or os.urandom()
random.seed(12345)        # Seed based on integer given
random.seed(b'bytedata')  # Seed based on byte data

# random.uniform(), random.gauss(), ssl_RAND_bytes()


# 3.12 Converting Days to Seconds, and Other Basic Time Conversions
from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c)
print(c.days)
print(c.seconds)
print(c.seconds/3600)
print(c.total_seconds()/3600)

from datetime import datetime
a = datetime(2012, 9, 23)
print(a + timedelta(days=10))
b = datetime(2012, 12, 21)
d = b - a
print(d)
print(d.days)

now = datetime.today()
print(now)
print(now + timedelta(minutes=10))

a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)    # 2012.2.29 있음
print((a-b).days)

c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)    # 2013.2.29 없음
print((c-d).days)

a = datetime(2012, 9, 23)
try:
    print(a + timedelta(months=1))
except TypeError as e:
    print(e)

from dateutil.relativedelta import relativedelta
a = datetime(2012, 9, 23)
print(a)
print(a+relativedelta(months=+1))
print(a + relativedelta(months=+4))

# Time between two dates
a = datetime(2012, 9, 23)
b = datetime(2012, 12, 21)
d = b -a
print(d)
d = relativedelta(b, a)
print(d, d.months, d.days)


# 3.13 Determining Last Friday's Date
from datetime import datetime, timedelta
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']
def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    print('day_num: ', day_num)
    day_num_target = weekdays.index(dayname)
    print('day_num_target: ', day_num_target)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date
print(datetime.today())
print(get_previous_byday('Sunday'))
print(get_previous_byday('Sunday', datetime(2012, 12, 21)))

from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
d = datetime.now()
k = datetime.today()
print(d)
print(k)

print(d + relativedelta(weekday=FR))  # Next Friday
print(d + relativedelta(weekday=FR(-1)))  # Last Friday


# 3.14 Finding the Date Range for the Current Month
from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
        print('start_date: ', start_date)
    else:
            start_date = start_date.replace(day=1)

    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    print('days_in_month: ', _, days_in_month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)

a_day = timedelta(days=1)
input_date = date(2019, 3, 20)
first_day, last_day = get_month_range(input_date)
while first_day < last_day:
    print(first_day)
    first_day += a_day

def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step

for d in date_range(datetime(2012, 9, 1), datetime(2012,10,1), timedelta(hours=12)):
    print(d)

def date_range(start, stop, step):
    while start < (stop + timedelta(days=1)):
        yield start
        start += step

for d in date_range(date(2012, 9, 1), date(2012,9,30), timedelta(days=1)):
    print(d)


# 3.15 Converting Strings into Datetimes
# datetime.strptime()
# datetime.strftime()
from datetime import datetime
text = '2020-03-08'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
x = datetime.today()

diff = z - y
print(diff)

diff1= x - y
print(diff1)

print(z)
nice_z = datetime.strftime(z, '%A %B %d %Y')
print(nice_z)

# This function runs over seven times faster than datetime.strptime().
from datetime import datetime
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))
print(parse_ymd('2020-03-20'))


# 3.16 Manipulating Dates Involving Time Zones
# You had a conference call scheduled for December 21, 2012, at 9:30 a.m in Chicago.
# 다른 곳에 있는 참여자들의 local time ?
# pytz module
from datetime import datetime
from pytz import timezone
d = datetime(2012, 12, 21, 9, 30, 0)
print(d)

central = timezone('US/Central')   # Localize the date for Chicago
loc_d = central.localize(d)
print(loc_d)

bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

# Consider Daylight saving time
d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)
later = loc_d + timedelta(minutes=30)
print(later)    # Wrong Result

from datetime import timedelta
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)

#print(loc_d)
#utc_d = loc_d.astimezone(pytz.utc)
#print(utc_d)
