# =======================================================================#
# =======================================================================#
# =======================================================================#

# =======================================================================#
# =======================================================================#
# =======================================================================#

# =======================================================================#
# =======================================================================#
# =======================================================================#



# =======================================================================#
# =======================================================================#
# =======================================================================#
# A regular polygon has n number of sides. Each side has length s.
#
# The area of a regular polygon is: 0.25*n*s*s / (math.tan(math.pi/n))
# The perimeter of a polygon is: length of the boundary of the polygon
# Write a function called polysum that takes 2 arguments, n and s.
# This function should sum the area and square of the perimeter of the regular polygon.
# The function returns the sum, rounded to 4 decimal places.

import math
def polysum(n,s):
    p = n *s
    area = 0.25*n*s*s / (math.tan(math.pi/n))
    return round(area + p*p, 4)

print(polysum(3,5))


# # =======================================================================#
# # =======================================================================#
# # =======================================================================#
#
# # aStr = "ciijlmnoqqrrrswz"
# # print(aStr)
# # print(len(aStr))
# # print((len(aStr)/2))
# # print(len(aStr)//2)
# # print(aStr[len(aStr)//2])
# # print(aStr[:len(aStr)//2])
#
#
# def isIn(char, aStr):
#     '''
#     char: a single character
#     aStr: an alphabetized string
#
#     returns: True if char is in aStr; False otherwise
#     '''
#     # Your code here
#
#     if len(aStr) < 1:
#         return False
#     elif len(aStr) == 1 and aStr[len(aStr) // 2] != char:
#         return False
#     elif aStr[len(aStr) // 2] == char:
#         print(aStr[len(aStr) // 2])
#         return True
#     elif aStr[len(aStr) // 2] > char:
#         print("character is smaller than mid letter #: " + str(len(aStr)//2) + aStr[len(aStr)//2] + '. ' + aStr[:len(aStr) // 2])
#         return isIn(char, aStr[:len(aStr) // 2])
#     elif aStr[len(aStr) // 2] < char:
#         print("character is LARGER than mid letter #: " + str(len(aStr)//2) + aStr[len(aStr)//2] + '. ' + aStr[len(aStr) // 2:])
#         return isIn(char, aStr[len(aStr)//2:])
#     else:
#         return False
#
# print(isIn('b', 'aaddehjkknnoopqrwwz'))

# =======================================================================#
# =======================================================================#
# =======================================================================#

# def gcdRecur(a, b):
#     '''
#     a, b: positive integers
#
#     returns: a positive integer, the greatest common divisor of a & b.
#     '''
#     # Your code here
#
#     if b == 0:
#         return a
#     else:
#         print("a is: " + str(a) + " b is: " + str(b))
#         print(" a % b = " + str(a%b))
#         print("will now take gcd("+str(b)+',' + str(a%b)+')')
#         return gcdRecur(b, a % b)
#
# print(gcdRecur(24, 9))

# x = 24 % 9
# print(x)

# def gcdIter(a, b):
#     '''
#     a, b: positive integers
#
#     returns: a positive integer, the greatest common divisor of a & b.
#     '''
#     # Your code here
#
#     if a > b:
#         i = b
#         while i > 0:
#             if a % i == 0 and b % i == 0:
#                 return i
#             else:
#                 #print("reducing i: " + str(i))
#                 i -= 1
#     else:
#         i = a
#         while i > 0:
#             if a % i == 0 and b % i == 0:
#                 return i
#             else:
#                 #print("reducing i: " + str(i))
#                 i -= 1
#
#
# print(gcdIter(24,24))

# def iterPower(base, exp):
#     '''
#     base: int or float.
#     exp: int >= 0
#
#     returns: int or float, base^exp
#     '''
#     # Your code here
#     product = base
#
#     if exp == 0:
#         return 1
#     else:
#         for i in range(1, exp):
#             #print("my exp now is: " + str(i), "base is: " + str(product))
#             i+=1
#             product = product * base
#             #print("AFTER iteration my exp now is: " + str(i), "base is: " + str(product))
#         return product
#
# print(iterPower(3,3))
# print(iterPower(5,6))

# x = 12
# def g(x):
#       x = x + 1
#       def h(y):
#           return x + y
#       return h(6)
# g(x)

### calling g(x) will output 19 ###
#
# x is defined as 12 before function def, so when g(x) is called it takes 12 into the function
# inside g(x becomes x+1 ==> 13
# because x is now defined 13 when:
# return h(6) ==> return x + y ==> 13 + 6 = 19

# def foo(x, y=5):
#     def bar(x):
#         return x + 1
#
#     return bar(y * 2)
#
#
# foo(3)
#
# 11
# correct
#
#
# def foo(x, y=5):
#     def bar(x):
#         return x + 1
#
#     return bar(y * 2)
#
#
# foo(3, 0)
#
# 1
# correct
#
#
# def foo(x):
#     def bar(z, x=0):
#         return z + x
#
#     return bar(3, x)
#
#
# foo(2)
#
# 5
# correct
#
#
# def foo(x):
#      def bar(z, x=0):
#          return z + x
#
#      return bar(3)
#
# print(foo(5))
#
#
# foo(5)
#
# 3
# correct
