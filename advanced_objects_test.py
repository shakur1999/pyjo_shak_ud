# Advanced Python Objects Tes Advanced Numbers

#Problem 1: Convert 1024 to binary and hexadecimal representation
bin(1024)

# Problem 2: Round 5.23222 to two decimal places
round(5.23222, 2)

# Advanced Strings
# Problem 3: Check if every letter in the string s is lower case
s = 'hello how are you Mary, are you feeling okay?'
s.islower()

# Problem 4: How many times does the letter 'w' show up in the string below?
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
s.count("w")

# Advanced Sets
# Problem 5: Find the elements in set1 that are not in set2:

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
set1.difference(set2)

# Problem 6: Find all elements that are in either set:
set.union(set2)


# Advanced Dictionaries
# Problem 7: Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension.
{x:x**3 for x in range(5)}

# Advanced Lists
# Problem 8: Reverse the list below:
list1 = [1,2,3,4]
list1.reverse()

# Problem 9: Sort the list below:
list2 = [3,4,2,5,1]
list2.sort()

# ===================== END =============================================================================

