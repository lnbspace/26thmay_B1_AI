Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> if  = 20
SyntaxError: invalid syntax
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> len(keyword.kwlist)
36
>>> a = 20
>>> a1 = 20;
>>> a1 = 30;
>>> a2 = 40; b = 30
>>> a = b = 3
>>> a
3
>>> b
3
>>> a,b = 30,33
>>> a
30
>>> b
33
>>> # This is a comment
>>> s = "Python"
>>> s1 = Python
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s1 = Python
NameError: name 'Python' is not defined
>>> print(a)
30
>>> print(a,b,a1,a2)
30 33 30 40
>>> s
'Python'
>>> print(s)
Python
>>> 6<((7>8)||(4>5))
SyntaxError: invalid syntax
>>> 3&4
0
>>> 3|4
7
>>> 3^4
7
>>> 2&3
2
>>> 2|3
3
>>> 2^3
1
>>> 8<<2
32
>>> 8>>2
2
>>> 16<<3
128
>>> 16 * (2**3)
128
>>> s
'Python'
>>> 'on' in s
True
>>> 'z' not in s
True
>>> help(id)
Help on built-in function id in module builtins:

id(obj, /)
    Return the identity of an object.
    
    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)

>>> m = 10
>>> n = 20
>>> p = 10
>>> id(m)
2544072878672
>>> id(n)
2544072878992
>>> id(p)
2544072878672
>>> m is n
False
>>> m is p
True
>>> 7 << 3
56
>>> 7 * (2**3)
56
>>> 7 // (2**3)
0
>>> 7 >> 3
0
>>> id(m) == id(n)
False
>>> 7>>1
3
>>> ###########################################
>>> # INTEGER
>>> ##########################################
>>> # int
>>> ##########################################
>>> a = 10
>>> type(a)
<class 'int'>
>>> ###########################################
>>> # FLOAT
>>> ###########################################
>>> b = 10.3
>>> type(b)
<class 'float'>
>>> ###########################################
>>> # FLOAT
>>> # Complex
>>> ###########################################
>>> c = 4+3j
>>> type(c)
<class 'complex'>
>>> ###########################################
>>> 
>>> 
>>> 
>>> # String #################################
>>> s = 'hello this is python string'
>>> type(s)
<class 'str'>
>>> print(s)
hello this is python string
>>> s
'hello this is python string'
>>> s1 = "hello this is python string"
>>> type(s1)
<class 'str'>
>>> s2 = '''Hello this is python string'''
>>> type(s2)
<class 'str'>
>>> s3 = 'I have one line
SyntaxError: EOL while scanning string literal
>>> s3 = '''I have one line
and now i can write the other line
as well as more lines
in my code'''
>>> type(s3)
<class 'str'>
>>> print(s3)
I have one line
and now i can write the other line
as well as more lines
in my code
>>> s3
'I have one line\nand now i can write the other line\nas well as more lines\nin my code'
>>> s4 = """I have one line
and now i can write the other line
as well as more lines
in my code"""
>>> type(s4)
<class 'str'>
>>> s5 = 'I feel like, it shouldn\'t be like that'
>>> s5
"I feel like, it shouldn't be like that"
>>> s6 = "I feel like, it shouldn't be like that"
>>> s6
"I feel like, it shouldn't be like that"
>>> 
>>> 
>>> #########################################
>>> ## LIST
>>> #########################################
>>> # Collection of Heterogenous Elements
>>> 
>>> a = [4,'Hello',5.6, [7,'H']]
>>> type(a)
<class 'list'>
>>> print(a)
[4, 'Hello', 5.6, [7, 'H']]
>>> len(a)
4
>>> len(s)
27
>>> s
'hello this is python string'
>>> #########################################
>>> ## Tuple - Collection of Hetergenous Elemnts (Immutable)
>>> ########################################################
>>> b = (4,'Hello',5.6, [7,'H'], (5,7,3))
>>> type(b)
<class 'tuple'>
>>> len(b)
5
>>> print(b)
(4, 'Hello', 5.6, [7, 'H'], (5, 7, 3))
>>> b1 = 3,'wow',87
>>> type(b1)
<class 'tuple'>
>>> b2 = (45)
>>> type(b2)
<class 'int'>
>>> b2 = (45,)
>>> type(b2)
<class 'tuple'>
>>> 
>>> #########################################
>>> ## Dictionary - Collection of Hetergenous Elements; Structure (mutable)
>>> ##########################################
>>> # key:value pair
>>> d= {'name':['a','b','c'], 'price':[4,5,4,56,]}
>>> type(d)
<class 'dict'>
>>> print(d)
{'name': ['a', 'b', 'c'], 'price': [4, 5, 4, 56]}
>>> len(d)
2
>>> #########################################
>>> ## Set - collection of unique elements
>>> #########################################
>>> p = {45,45,65,5,34,87,45,'hello','hello','Hello'}
>>> type(p)
<class 'set'>
>>> print(p)
{65, 34, 5, 87, 'Hello', 45, 'hello'}
>>> len(b1)
3
>>> #########################################
>>> ## Bool - True, False
>>> #########################################
>>> true
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    true
NameError: name 'true' is not defined
>>> True
True
>>> # anything which is non-zero of non-empty -> True
>>> # anything zero or empty -> False
>>> bool(4)
True
>>> bool('hello')
True
>>> bool(None)
False
>>> bool(0)
False
>>> bool('')
False
>>> bool(' ')
True
>>> bool([])
False
>>> bool(())
False
>>> bool({})
False
>>> 7>4
True
>>> 7 and 7
7
>>> a = {}; type(a)
<class 'dict'>
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #################################################
>>> # String - immuatble
>>> #
>>> 
>>> s
'hello this is python string'
>>> s = 'hello this is python string'
>>> len(s)
27
>>> s[0]
'h'
>>> s[6]
't'
>>> s[-1]
'g'
>>> s[26]
'g'
>>> # slicing
>>> # [begin:ending(not included):gap(with direction)]
>>> s[0:5:1]
'hello'
>>> s[14:20:1]
'python'
>>> s[6:13:1]
'this is'
>>> s[-21:-14:1]
'this is'
>>> s[6:-14:1]
'this is'
>>> s[-21:13:1]
'this is'
>>> s[-6:27:1]
'string'
>>> s[-6:27:]
'string'
>>> s[-6:27]
'string'
>>> s[-6:]
'string'
>>> s[:5]
'hello'
>>> #
>>> s[-1:-7:-1]
'gnirts'
>>> s[:-7:-1]
'gnirts'
>>> s
'hello this is python string'
>>> s[5::-1]
' olleh'
>>> s[4::-1]
'olleh'
>>> s[::-1]
'gnirts nohtyp si siht olleh'
>>> s[-8:-19:-1]
'nohtyp si s'
>>> s[-8:-17:-1]
'nohtyp si'
>>> # Change
>>> s[0]
'h'
>>> s[0] = 'K'
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    s[0] = 'K'
TypeError: 'str' object does not support item assignment
>>> del s[0]
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    del s[0]
TypeError: 'str' object doesn't support item deletion
>>> #
>>> #
>>> # str + str ====> strstr
>>> 'hello' + 'bye'
'hellobye'
>>> 'hello'*3
'hellohellohello'
>>> 
>>> s
'hello this is python string'
>>> s += ' here'
>>> s
'hello this is python string here'
>>> s[14]
'p'
>>> s = s[:14]+'a new '+s[14:]
>>> s
'hello this is a new python string here'
>>> 