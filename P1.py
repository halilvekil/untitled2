# s = 'azcbobobegghakl'
# numVowels = 0
#
# for char in s:
#     if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
#         numVowels += 1
#
# print('Number of vowels: ' + str(numVowels))

s = 'bobobobobobobobobob'
# b = 0
# o = 0
# third = 0
#
# for letter in s:
#     print('I am at the letter: ' + str(letter))
#     if letter == 'b' and o==0:
#         b=1
#     elif letter == 'o' and b==1:
#         b = 0
#         o = 1
#         print('I am at the letter: ' +str(letter) + ' and found a BO')
#     elif letter == 'b' and o==1:
#         b=1
#         third += 1
#         print('I am at the letter: ' +str(letter) + ' and found a BOB!')
#     else:
#         b = 0
#         o = 0

index = ''
counter = 0
for letter in s:
    index = index + letter
    # print(index)
    if 'bob' in index:
        counter += 1
        index = 'b'
print('Number of times bob occurs is: ' + str(counter))

# print('Number of times bob occurs is: ' + str(third))
#
# str1 = 'hello'
# str2 = ','
# str3 = 'world'
# str4 = str1 + str3
# print(str4)
# check = 'low' in str4
# print(check)
# str3[:3]
