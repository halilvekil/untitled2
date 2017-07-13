def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here

    if b == 0:
        return a
    else:
        print("a is: " + str(a) + " b is: " + str(b))
        print(" a % b = " + str(a%b))
        print("will now take gcd("+str(b)+',' + str(a%b)+')')
        return gcdRecur(b, a % b)

print(gcdRecur(24, 9))

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
