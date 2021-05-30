Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'hi\
this is second line\
this is third line'
>>> s
'hithis is second linethis is third line'
>>> print(s)
hithis is second linethis is third line
>>> s1 = 'this\twow'
>>> print(s1)
this	wow
>>> s = '''hi
this is second line
this is third line'''
>>> print(s)
hi
this is second line
this is third line
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day3/script_file.py ============
One line
two line
three line
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day3/script_file.py ============
One line
two line
three line
2
>>> 4+5
9
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day3/script_file.py ============
2
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day3/script_file.py ============
2
>>> ## List
>>> a = [45,88,56, 'Hello']
>>> print(a)
[45, 88, 56, 'Hello']
>>> type(a)
<class 'list'>
>>> a
[45, 88, 56, 'Hello']
>>> len(a)
4
>>> # access
>>> a[0]
45
>>> a[-1]
'Hello'
>>> a[:2]
[45, 88]
>>> a[-1]
'Hello'
>>> a[-1][0]
'H'
>>> b = [5,6,7,[5,7,[['Go'],'Nice',9]]]
>>> len(b)
4
>>> b[3]
[5, 7, [['Go'], 'Nice', 9]]
>>> b[-1]
[5, 7, [['Go'], 'Nice', 9]]
>>> b[-1][1]
7
>>> b[-1][-1]
[['Go'], 'Nice', 9]
>>> b[-1][-1][0]
['Go']
>>> b[-1][-1][0][0]
'Go'
>>> b[-1][-1][0][0][0]
'G'
>>> # modify
>>> b[0] = 55
>>> b
[55, 6, 7, [5, 7, [['Go'], 'Nice', 9]]]
>>> del b[1]
>>> b
[55, 7, [5, 7, [['Go'], 'Nice', 9]]]
>>> 
>>> 
>>> b*3
[55, 7, [5, 7, [['Go'], 'Nice', 9]], 55, 7, [5, 7, [['Go'], 'Nice', 9]], 55, 7, [5, 7, [['Go'], 'Nice', 9]]]
>>> a*2
[45, 88, 56, 'Hello', 45, 88, 56, 'Hello']
>>> a + b
[45, 88, 56, 'Hello', 55, 7, [5, 7, [['Go'], 'Nice', 9]]]
>>> 
>>> a
[45, 88, 56, 'Hello']
>>> a += [99]
>>> a
[45, 88, 56, 'Hello', 99]
>>> 
>>> 
>>> a += ['hi',78]
>>> a
[45, 88, 56, 'Hello', 99, 'hi', 78]
>>> a += 'good'
>>> a
[45, 88, 56, 'Hello', 99, 'hi', 78, 'g', 'o', 'o', 'd']
>>> 
>>> 
>>> 
>>> 
>>> #################
>>> a = a[:3] + [100] + a[3:]
>>> a
[45, 88, 56, 100, 'Hello', 99, 'hi', 78, 'g', 'o', 'o', 'd']
>>> 
>>> 
>>> #######################################################
>>> # Built-in functions for String & Lists
>>> 
>>> # str
>>> s = 'Hi Its Python Here'
>>> s.capitalize()
'Hi its python here'
>>> s1 = s.capitalize()
>>> s1
'Hi its python here'
>>> s.count('e')
2
>>> s.find('s')
5
>>> s.find('e')
15
>>> s.index('e')
15
>>> s.index('z')
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> s.find('z')
-1
>>> s.isalpha()
False
>>> s
'Hi Its Python Here'
>>> 'hello'.isalpha()
True
>>> 'hello '.isalpha()
False
>>> '123'.isnumeric()
True
>>> '123 '.isnumeric()
False
>>> s.split()
['Hi', 'Its', 'Python', 'Here']
>>> s.split('t')
['Hi I', 's Py', 'hon Here']
>>> s.split('on')
['Hi Its Pyth', ' Here']
>>> 'abcd'.join('good')
'gabcdoabcdoabcdd'
>>> '-'.join('good')
'g-o-o-d'
>>> s
'Hi Its Python Here'
>>> s.split()
['Hi', 'Its', 'Python', 'Here']
>>> s.split()[::-1]
['Here', 'Python', 'Its', 'Hi']
>>> ' '.join(s.split()[::-1])
'Here Python Its Hi'
>>> s.startswith('H')
True
>>> s.startswith('dsfs')
False
>>> s.strip('H')
'i Its Python Here'
>>> s1 = '     hi        '
>>> s1.strip()
'hi'
>>> a = 30
>>> b = 40
>>> k = 'when we add {} and {} together, we get {}'.format(a,b,a+b)
>>> print(k)
when we add 30 and 40 together, we get 70
>>> k1 = 'we got, {0} and {1}; when we add {0} and {1} together, we get {2}'.format(a,b,a+b)
>>> print(k1)
we got, 30 and 40; when we add 30 and 40 together, we get 70
>>> 
>>> 
>>> # list
>>> a = [45,76,34,9,100]
>>> a.append(65)
>>> a
[45, 76, 34, 9, 100, 65]
>>> a.append(66,67)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    a.append(66,67)
TypeError: list.append() takes exactly one argument (2 given)
>>> a1 = a.append(87)
>>> a1
>>> a = a.append(87)
>>> print(a)
None
>>> a = [45,76,34,9,100]
>>> a.clear()
>>> a
[]
>>> a = [45,76,34,9,100]
>>> a1 = a
>>> a2 = a.copy()
>>> a1
[45, 76, 34, 9, 100]
>>> a2
[45, 76, 34, 9, 100]
>>> a2.append(55)
>>> a2
[45, 76, 34, 9, 100, 55]
>>> a
[45, 76, 34, 9, 100]
>>> a1.append(66)
>>> a1
[45, 76, 34, 9, 100, 66]
>>> a
[45, 76, 34, 9, 100, 66]
>>> a.append(88)
>>> a
[45, 76, 34, 9, 100, 66, 88]
>>> a3 = a.append(889)
>>> a3
>>> a
[45, 76, 34, 9, 100, 66, 88, 889]
>>> a.count(45)
1
>>> a.index(76)
1
>>> a.index(100)
4
>>> a.insert(5,73)
>>> a
[45, 76, 34, 9, 100, 73, 66, 88, 889]
>>> a.pop(3)
9
>>> a
[45, 76, 34, 100, 73, 66, 88, 889]
>>> a.remove(66)
>>> a
[45, 76, 34, 100, 73, 88, 889]
>>> a.sort()
>>> a
[34, 45, 73, 76, 88, 100, 889]
>>> help(a.extend)
Help on built-in function extend:

extend(iterable, /) method of builtins.list instance
    Extend list by appending elements from the iterable.

>>> 
>>> 
>>> ####################################################
>>> max(a)
889
>>> min(a)
34
>>> sum(a)
1305
>>> abs(a)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    abs(a)
TypeError: bad operand type for abs(): 'list'
>>> a
[34, 45, 73, 76, 88, 100, 889]
>>> ###########################################################################
>>> 
>>> # tuple
>>> t = (45,76,45,98,34,(6,7),'Right')
>>> type(t)
<class 'tuple'>
>>> print(t)
(45, 76, 45, 98, 34, (6, 7), 'Right')
>>> t
(45, 76, 45, 98, 34, (6, 7), 'Right')
>>> len(t)
7
>>> t[0]
45
>>> t[:4]
(45, 76, 45, 98)
>>> t[-3:-8:-1]
(34, 98, 45, 76, 45)
>>> 
>>> t[0]=3
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    t[0]=3
TypeError: 'tuple' object does not support item assignment
>>> del t[0]
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    del t[0]
TypeError: 'tuple' object doesn't support item deletion
>>> 
>>> t += ('go','thirty',444)
>>> t
(45, 76, 45, 98, 34, (6, 7), 'Right', 'go', 'thirty', 444)
>>> t += 'hello'
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    t += 'hello'
TypeError: can only concatenate tuple (not "str") to tuple
>>> 
>>> 45 in t
True
>>> 'z' in t
False
>>> 'o' in t
False
>>> g = 'Right'
>>> g in t
True
>>> 7 in t
False
>>> 7 in t[-5]
True
>>> t.count(45)
2
>>> t.index('go')
7
>>> 
>>> t1 = list(t)
>>> t1
[45, 76, 45, 98, 34, (6, 7), 'Right', 'go', 'thirty', 444]
>>> int('hey')
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    int('hey')
ValueError: invalid literal for int() with base 10: 'hey'
>>> int('45')
45
>>> ###################################################################
>>> d = {'color':['red','blue','green'],'price':[45,50,53]}
>>> len(d)
2
>>> type(d)
<class 'dict'>
>>> print(d)
{'color': ['red', 'blue', 'green'], 'price': [45, 50, 53]}
>>> 
>>> # accessing the elements
>>> d['color']
['red', 'blue', 'green']
>>> d['price']
[45, 50, 53]
>>> d['color'][1]
'blue'
>>> 
>>> # modifying the values
>>> d['price'] = [56,50,54]
>>> d
{'color': ['red', 'blue', 'green'], 'price': [56, 50, 54]}
>>> 
>>> # inserting a new key:value pair
>>> d['brand'] = ['A','B',]
'
>>> 
>>> d['brand'] = ['A','B','K']
>>> d
{'color': ['red', 'blue', 'green'], 'price': [56, 50, 54], 'brand': ['A', 'B', 'K']}
>>> # delete
>>> del d['color']
>>> d
{'price': [56, 50, 54], 'brand': ['A', 'B', 'K']}
>>> 
>>> d.keys()
dict_keys(['price', 'brand'])
>>> d.values()
dict_values([[56, 50, 54], ['A', 'B', 'K']])
>>> d.keys()[0]
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    d.keys()[0]
TypeError: 'dict_keys' object is not subscriptable
>>> list(d.keys())[0]
'price'
>>> 
>>> d['color']
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    d['color']
KeyError: 'color'
>>> d
{'price': [56, 50, 54], 'brand': ['A', 'B', 'K']}
>>> d.get('color')
>>> d.get('price')
[56, 50, 54]
>>> 
>>> 
>>> 'price' in d
True
>>> d
{'price': [56, 50, 54], 'brand': ['A', 'B', 'K']}
>>> {'price': [56, 50, 54], 'company': ['A', 'B', 'K']}
{'price': [56, 50, 54], 'company': ['A', 'B', 'K']}
>>> 
>>> ###
>>> d['company'] = d['brand']
>>> del d['brand']
>>> d
{'price': [56, 50, 54], 'company': ['A', 'B', 'K']}
>>> 
>>> ##
>>> d['Company'] = d.pop('company')
>>> d
{'price': [56, 50, 54], 'Company': ['A', 'B', 'K']}
>>> 
>>> d
{'price': [56, 50, 54], 'Company': ['A', 'B', 'K']}
>>> d2 = {'a':45,[666]:'wow}
      
SyntaxError: EOL while scanning string literal
>>> d2 = {'a':45,[666]:'wow'}
Traceback (most recent call last):
  File "<pyshell#233>", line 1, in <module>
    d2 = {'a':45,[666]:'wow'}
TypeError: unhashable type: 'list'
>>> d2 = {'a':45,666:'wow}
      
SyntaxError: EOL while scanning string literal
>>> d2 = {'a':45,666:'wow'}
>>> d+d2
Traceback (most recent call last):
  File "<pyshell#236>", line 1, in <module>
    d+d2
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> 
>>> 
>>> {**d, **d2}
{'price': [56, 50, 54], 'Company': ['A', 'B', 'K'], 'a': 45, 666: 'wow'}
>>> 
>>> 
>>> 
>>> 
>>> s = {4,5,7,3,4,4,4}
>>> s
{3, 4, 5, 7}
>>> print(s)
{3, 4, 5, 7}
>>> len(s)
4
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#248>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
>>> s1 = {8,7,4,5}
>>> s.add(9)
>>> a
[34, 45, 73, 76, 88, 100, 889]
>>> s
{3, 4, 5, 7, 9}
>>> s.remove(4)
>>> s
{3, 5, 7, 9}
>>> s.difference(s1)
{9, 3}
>>> s.union()
{9, 3, 5, 7}
>>> s.intersection()
{9, 3, 5, 7}
>>> 
>>> #############################################################################
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day3/script_file.py ============
Moderate
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day3/script_file.py ============
Huge
>>> 
============ RESTART: E:/TN/SITP21/26thMay_B1_AI_ML/day3/script_file.py ============
Huge
it is
>>> 