##########TUPLES##########
x = (1, 2, (3, 'John', 4), 'Hi')

print(x[-1][-1]) # i
print(x[-1][-2]) # H
#print(x[-1][2]) # ERROR IndexError: string index out of range
print(x[0:1]) #(1,)
print(3 in x)   ## FALSE: DOES NOT RECOGNIZE THE ELEMENTS OF THE TUPLE INSIDE TUPLE X
x[0] = 8    ## TypeError: 'tuple' object does not support item assignment //TUPLES ARE IMMUTABLE

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