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



