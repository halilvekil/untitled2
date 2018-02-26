animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}
animals['d'] = 'donkey'
for value in animals.items():
    print(animals.keys(),animals.values())

##USING MAP. A BUILT IN GENERAL PURPOSE mapper OR 'HOPPER'
map(abs,[1,-2,-4,5,-6,-8,11,-12])
for element in map(abs,[1,-2,-4,5,-6,-8,11,-12]):
    print element
print("STOP")

L1 = [12,43,12,1]
L2 = [45,3,3,63,6]
for element in map(min,L1,L2):
    print element
print("STOP")

##APPLYING A LIST OF FUNCTIONS TO A NUMBER

import math
def apply_Functions(L,x):
    for f in L:
        print (f(x))

apply_Functions([abs,int,math.factorial,math.tan],4)



##########LISTS##########

x = [1, 2, [3, 'John', 4], 'Hi']
print(x[0:1])                       ##!! THIS PRINTS OUT A LIST. NOT AN INT. OUTPUT: [1]
print(x[:4])

###THE "IS" OPERATOR!!###
# is operator tests. It tests if two variables point the same object, not if two variables have the same value.
#
# From the documentation for the is operator:
#
# The operators is and is not test for object identity: x is y is true if and only if x and y are the same object.

##CLONING A LIST##
cloneX = x[:]
print("this is the CLONE OF X: " + str(cloneX))
cloneX[2] = 'new #2'
print("this is the NEW CLONE OF X: " + str(cloneX))
print("BUT X REMAINS UNCHANGED: " + str(x))

x.remove('Hi')      ##Removes the specified element in the list. If it doesn't exist this will produce an error
print(x)
del(x[2])           ##Removes the specified element of the list
print(x)
print("Popping (removing last element)")
x.pop()
print(x)

q = "sakarya"
#q = list(q)
#print("list(q) \n" +q)
print(q)
print("***q.split('k')***")
q = q.split("k")                ##THE STRING HAS BECOME A LIST because of the split operation
                                ##SPLIT IS A STRING OPERATION, CANNOT BE APPLIED TO LIST
print(q)
q = '*'.join(q)
print("'*'.join(q)")
print(q)

q = "sakarya"
q = list(q)
print(q)
print(sorted(q))
print("q.sort()", q.sort(), q)
print(q.reverse(), q)
print('here I am')
print(q.sort)


##########TUPLES##########

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    oTup = ()
    for i in range(0, len(aTup)):
        if i % 2 == 0:
            oTup += (aTup[i],)
        i += 1
    return oTup

print(oddTuples((15, 1, (77,66,55,44), 15, 9, 15, 88)))


# x = (1, 2, (3, 'John', 4), 'Hi')
#
# print(x[-1][-1]) # i
# print(x[-1][-2]) # H
# #print(x[-1][2]) # ERROR IndexError: string index out of range
# print(x[0:1]) #(1,)
# print(3 in x)   ## FALSE: DOES NOT RECOGNIZE THE ELEMENTS OF THE TUPLE INSIDE TUPLE X
# x[0] = 8    ## TypeError: 'tuple' object does not support item assignment //TUPLES ARE IMMUTABLE

# spam = "7"
# spam = spam + "0"
# eggs = int(spam) + 3
# print(float(eggs))
# #73.0
#
# for i in range(10): ## starts from 0 --> 9
#     print(i)
#     i+=1
#
# list = [1, 1, 2, 3, 5, 8, 13]
# print(list[0])
#
#
# for var in list: #prints the whole list
#     print(var)