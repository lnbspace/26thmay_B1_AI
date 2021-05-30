##a = eval(input('Enter first number:'))
#b = eval(input('Enter second number:'))

# check if the value of a is divisible by b or not
##if a%b == 0:
##    print('Divisible')
##else:
##    print('Not Divisible')

# Using Ternary Operator
#print('Not divisible') if a%b else print('Divisible')
##print('Even') if not a%2 else print('odd')

##c = eval(input('Enter the third number:'))
# find the max of a,b,c
##if a>=b and a>=c:
##    print(a,'is biggest')
##elif b>=a and b>=c:
##    print(b,'is biggest')
##elif c>=a and c>=b:
##    print(c,'is biggest')

#####################################################
# WHILE Loops
#############

##a = 10
##while a:
##    print('good')
##    a -= 1
##    if a%3:
##        continue
##    print('wow')
##print('-'*30)  

##a = 10
##while a:
##    print('good')
##    a -= 1
##    if a%3:
##        break
##    print('wow')

#####################################################
# FOR Loops
#############

##a = [4,6,8,9]
##for i in a:
##    print(i, i*2)

##for i in a:
##    for j in range(1,i+1):
##        if j == 8:
##            break
##        print('$'*j)
##    else:
##        print('-'*20)
##print('='*25)
##for i in a:
##    for j in range(1,i+1):
##        if j == 8:
##            continue
##        print('$'*j)
##    else:
##        print('-'*20)

##for i in range(len(a)):
##    print(a[i])

#----------------------------------------------------
# zip, enumerate

#a = [4,5,76,8,9,13]
#d = {0:4, 1:5, 2:76.......}

##i = 0
##d = {}
##for v in a:
##    d[i] = v
##    i += 1
##
##print(d)

##d = {}
##for i,v in enumerate(a):
##    d[i] = v

##b = ['a','b','s','d','f','r']
##c = ['First','Second']
##
##z = zip(a,b)
##print(list(z))

##k = [['a',45,67,'Nice'],['b',415,637,'Niceone'],['c',1465,697,'Niiice']]
##n = ('FIRST','SECOND','THIRD','FOURTH')
####print(list(zip(*k)))
####print(list(zip(n,zip(*k))))
##d = dict(zip(n,zip(*k)))
##print(d)

#-------------------------------------------------
# List Comprehensions
##a = [4,5,6,7,5,3,56]
##print(a)


#-- Double the values of a
# without comprehension
##b = []
##for i in a:
##    b.append(i*2)


# with comprehension
##b = [i*2 for i in a]
##print(b)

#-- Find the even numbers from a into another list
# without comprehension
##b=[]
##for i in a:
##    if not i%2:
##        b.append(i)

# with comprehension
##b = [i for i in a if not i%2]        
##print(b)

#-- find the even numbers and multiply even values with 10 if they are less than 10

# without comprehension
##b = []
##for i in a:
##    if not i%2:
##        if i<10:
##            b.append(i*10)
##        else:
##            b.append(i)
##print(b)

# with comp
##b = [i*10 if i<10 else i for i in a if not i%2]
##print(b)
        

#####-- Dictionary Comprehension
##d = {i:v for i,v in enumerate(a)}
##print(d)
##
##d1 = {i:[v,v**2] for i,v in enumerate(a)}
##print(d1)

##================================================================================
##s = input('enter any characters:')
####s = 'abthabbthht'
####d = {'a':2, 'b':3,'h':3,'t':3}
##d = {i:s.count(i) for i in s}
##print(d)

# TASK:
#  Find the count of each character
#  Check if all the counts are same or at-most one character
#   is one extra than all the others, Its MYSTRING else NOT MYSTRING
#
# Input: aaabbbccc
# Output: MYSTRING
#
# Input: aaaabbbccc
# OUTPUT: MYSTRING
#
# Input: aabbbccc
# OUTPUT: NOT MYSTRING


##================================================================================















































