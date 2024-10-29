# Example 09: Merging Dictionary 
# You can merge dictionaries using the update() method or the ** operator in Python 3.9+.

# Example Dictionaries
dict1 = {'name':'john','age':26}
dict2 = {'city':'Dhaka','country':'Bangladesh'}

# Merging using update()
dict1.update(dict2)


# Printing the merged dictionary 
print('Merged dictionary:',dict1)