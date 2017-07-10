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
def foo(x):
     def bar(z, x=0):
         return z + x

     return bar(3)

print(foo(5))
#
#
# foo(5)
#
# 3
# correct
