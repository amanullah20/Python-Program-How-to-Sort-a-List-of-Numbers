# Example 5: List of Tuples to Dictionary
# Converting a list of tuples into a dictionary using a loop.

# Example list of tuples
tuple_list = [('parrots', 10), ('peacock', 20), ('humming birds', 30), ('ducks', 40)]

# Converting to a dictionary
result_dict = {key: value for key, value in tuple_list}

print('Dictionary from List of Tuples:', result_dict)
