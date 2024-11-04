# Example 9: Dictionary Filtering Based on Conditions
# Filtering a dictionary to retain only key-value pairs that satisfy a condition.

# Example dictionary
scores = {'Anna': 15, 'Simon': 27, 'Christin': 19, 'Daniel': 46}

# Filtering to retain scores >= 80
filtered_scores = {name: score for name, score in scores.items() if score >= 30}

print('Filtered Scores:', filtered_scores)
