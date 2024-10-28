# Example 06 : Set Difference
# The difference() method returns a new set containing elements present in one set but not in the other.

# Yor can also use the - operator to perform the differences operation.

# Example sets

set1 = {1, 2, 3}
set2 = {2, 3, 4}

# Performing difference (elements is set1 but not in set2)
difference_set = set1.difference(set2)

# Printing the difference set
print('Difference of Sets : ', difference_set)
