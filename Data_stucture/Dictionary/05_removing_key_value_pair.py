# Example 05: Removing key-value Pairs from a Dictionary 
# You Can remove key-value pairs using the pop() method , which removes the specified key and returns its value.
# The del keyword can also be used to remove a specific key or clear() to remove all items.

# Example Dictionary 
my_dict = {'name':'aman','age':26,'city':'mymensingh'}

# Removing a key-value pair 
age = my_dict.pop('age')

# Printing the dictionary after removal 
print('Dictionary after removal:',my_dict)
print('removed age:',age)