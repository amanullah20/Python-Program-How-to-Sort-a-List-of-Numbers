# Example 09 : Sorting a Tuple
# Tuples are immutable and cannot be sorted directly.
# To sort a tuple,you need to convert it to a list , sort it and convert it back to a tuple.

# Example tuple
number_tuple = (4, 5, 2, 6, 1, 9)

# Sorting by converting to a list
sorted_list = sorted(number_tuple)
sorted_tuple = tuple(sorted_list)

# Printing the sorted tuple
print('sorted tuple:', sorted_tuple)