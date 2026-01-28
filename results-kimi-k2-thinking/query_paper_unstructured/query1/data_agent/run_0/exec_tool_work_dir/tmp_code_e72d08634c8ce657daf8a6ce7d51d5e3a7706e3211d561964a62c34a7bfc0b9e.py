code = """import json
import re

# Load the MongoDB results from the file path stored in var_functions.query_db:4
import pandas as pd

# Read the full result from the JSON file
result_file = '/tmp/tmp7q9h_0i5.json'
with open(result_file, 'r') as f:
    paper_docs = json.load(f)

# Extract titles from filenames (remove .txt extension)
# Also check if the paper is actually about food domain
food_papers = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    # Extract title (filename without .txt)
    title = re.sub(r'\.txt$', '', filename)
    
    # Check if this is actually a food domain paper
    # Look for evidence of food domain in the text
    # Patterns to look for: explicit mention of food domain, food tracking, dietary, nutrition, etc.
    food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie', 'dietary']
    text_lower = text.lower()
    
    # Check if any food keyword appears in context of domain/research focus
    is_food_paper = False
    for keyword in food_keywords:
        if keyword in text_lower:
            # Additional check: ensure it's not just a casual mention but part of domains studied
            if 'domain' in text_lower or 'track' in text_lower or 'tracking' in text_lower:
                is_food_paper = True
                break
    
    if is_food_paper:
        food_papers.append(title)

print(f"Found {len(food_papers)} papers in food domain")
print(f"First few titles: {food_papers[:5]}")

# Store the food paper titles in a variable for the next query
print('__RESULT__:')
print(json.dumps(food_papers))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence']}

exec(code, env_args)
