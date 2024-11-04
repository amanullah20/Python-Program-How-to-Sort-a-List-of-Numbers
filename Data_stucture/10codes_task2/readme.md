"""
# 01. Stationeries Nested List Manipulation

This script demonstrates various operations on a nested list structure in Python.

## Structure
- `stationaries`: A nested list containing categories of stationery items.

## Operations

1. **Accessing a Nested Element**
   - Retrieves a specific nested element within the list.
   - `nested_element = stationaries[1][2][1]` accesses 'stapler' within the nested list.

2. **Modifying a Nested Element**
   - Updates a specific element within the list.
   - `stationaries[2][1] = 'BOXES'` replaces 'calculator' with 'BOXES'.

3. **Flattening the Nested List**
   - Converts the nested list into a single-level list.
   - `flattened_list` uses a nested list comprehension to flatten `stationaries`.

## Output
- Prints the accessed element, the modified list, and the flattened list for verification.

"""

"""
# 02. Tuple Unpacking Example

This script demonstrates unpacking a tuple into multiple variables in Python.

## Structure
- `person_info`: A tuple containing personal information (name, age, job, and address).

## Operations

1. **Unpacking Tuple into Variables**
   - Unpacks specific elements of the tuple into variables (`name` and `age`).
   - Uses the `*` operator to capture remaining elements into `other_details`.
   - `name, age, *other_details = person_info` assigns 'Ruben' to `name`, 18 to `age`, and the remaining items to `other_details`.

## Output
- Prints the unpacked values: `Name`, `Age`, and `Other Details` for verification.

"""

"""
# 03. Set Comprehension with Condition Example

This script demonstrates creating a set using comprehension with a condition to filter elements.

## Structure
- `numbers`: A list of integers from 1 to 10.

## Operations

1. **Creating a Set with Condition**
   - Uses set comprehension to create a set of numbers that are divisible by 5.
   - `{num for num in numbers if num % 5 == 0}` adds `num` to `even_set` only if `num` is divisible by 5.

## Output
- Prints the resulting set, showing only numbers that meet the condition (divisible by 5).

"""

"""
# 04. Dictionary Merging with Comprehension Example

This script demonstrates merging two dictionaries and modifying values using dictionary comprehension in Python.

## Structure
- `fruit_box1` and `fruit_box2`: Dictionaries representing quantities of different fruits in two boxes.

## Operations

1. **Merging and Modifying Values**
   - Merges `fruit_box1` and `fruit_box2`, summing quantities for any fruits present in both dictionaries.
   - `{key: fruit_box1.get(key, 0) + fruit_box2.get(key, 0) for key in set(fruit_box1) | set(fruit_box2)}`:
     - Combines keys from both dictionaries using `set(fruit_box1) | set(fruit_box2)`.
     - Uses `get(key, 0)` to fetch values, defaulting to 0 if a fruit is absent in one dictionary.
     - Sums values from both dictionaries for each fruit.

## Output
- Prints the merged dictionary with updated quantities for each fruit.

"""

"""
# 05. List of Tuples to Dictionary Conversion Example

This script demonstrates converting a list of tuples into a dictionary using a loop.

## Structure
- `tuple_list`: A list of tuples where each tuple contains a key (bird type) and a value (quantity).

## Operations

1. **Converting List of Tuples to Dictionary**
   - Uses dictionary comprehension to convert `tuple_list` into `result_dict`.
   - `{key: value for key, value in tuple_list}` iterates over each tuple, assigning `key` to the first element and `value` to the second element, storing them in `result_dict`.

## Output
- Prints the dictionary created from the list of tuples, displaying each bird type with its corresponding quantity.

"""

"""
# 06. Set Operations with Multiple Sets Example

This script demonstrates performing union, intersection, and symmetric difference operations on multiple sets in Python.

## Structure
- `set1`, `set2`, `set3`: Three sets of integers with some overlapping elements.

## Operations

1. **Union of Sets**
   - Combines all unique elements from `set1`, `set2`, and `set3`.
   - `union_result = set1 | set2 | set3`

2. **Intersection of Sets**
   - Finds elements that are common to `set1`, `set2`, and `set3`.
   - `intersection_result = set1 & set2 & set3`

3. **Symmetric Difference of Sets**
   - Includes elements that are unique to each set, excluding those found in all three.
   - `symmetric_difference_result = set1 ^ set2 ^ set3`

## Output
- Prints the results of each operation: `Union of Sets`,

  """
# 07. Dictionary with Nested Structures Example

This script demonstrates accessing and modifying elements within a dictionary containing nested structures.

## Structure
- `nested_dict`: A dictionary with nested dictionaries and lists, representing information about a person.

## Operations

1. **Accessing Nested Elements**
   - Retrieves the value of a nested element (city).
   - `city = nested_dict['person']['details']['city']` accesses the 'city' key within nested dictionaries.

2. **Modifying a Nested Element**
   - Appends a new skill to the list of skills in the nested structure.
   - `nested_dict['person']['details']['skil

"""
# 08. List Comprehension with Conditional Nesting Example

This script demonstrates using list comprehension with nested loops and conditions to filter and flatten elements from a nested list (matrix).

## Structure
- `matrix`: A 2D list (matrix) with three rows of numbers.

## Operations

1. **Flattening and Filtering Even Numbers**
   - Uses list comprehension to iterate over each row and each number within `matrix`.
   - `[num for row in matrix for num in row if num % 2 == 0]`:
     - Loops over each `row` in `matrix` and then each `num` in `row`.
     - Includes `num` in `even_flattened` only if `num` is even (`num % 2 == 0`).

## Output
- Prints a flattened list containing only the even numbers from the matrix.

"""

"""
# 09.  Dictionary Filtering Based on Conditions Example

This script demonstrates filtering a dictionary to retain only key-value pairs that meet a specific condition.

## Structure
- `scores`: A dictionary containing names as keys and corresponding scores as values.

## Operations

1. **Filtering Dictionary by Condition**
   - Uses dictionary comprehension to create a new dictionary with entries where the score is 30 or higher.
   - `filtered_scores = {name: score for name, score in scores.items() if score >= 30}`:
     - Iterates over each key-value pair in `scores`.
     - Retains pairs where `score >= 30`.

## Output
- Prints the filtered dictionary containing only names with scores 30 or above.

"""

"""
# 10. Tuple Comprehension using Generator Expression Example

This script demonstrates creating a tuple using a generator expression to include elements that meet a specific condition.

## Structure
- `numbers`: A range of integers from 1 to 19.

## Operations

1. **Creating a Tuple of Squares of Even Numbers Divisible by 3**
   - Uses a generator expression to calculate squares of numbers in `numbers` that are divisible by 3.
   - `even_squares = tuple(x**2 for x in numbers if x % 3 == 0)`:
     - Loops over each number in `numbers`, checks if it’s divisible by 3, and, if true, calculates its square.
     - Wraps the result in `tuple()` to create a tuple from the generator expression.

## Output
- Prints the tuple containing squares of numbers divisible by 3 from the specified range.

"""
