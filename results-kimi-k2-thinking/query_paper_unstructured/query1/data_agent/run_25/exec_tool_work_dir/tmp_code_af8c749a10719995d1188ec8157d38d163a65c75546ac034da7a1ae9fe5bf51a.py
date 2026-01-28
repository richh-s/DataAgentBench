code = """import json

# Get the result from storage
food_papers = locals()['var_functions.query_db:2']

print(f"Found {len(food_papers)} papers mentioning 'food'")

# Extract titles from filenames (remove .txt extension)
food_titles = []
for paper in food_papers:
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]  # Remove .txt
        food_titles.append(title)

print(f"Extracted {len(food_titles)} titles")

# Print result in required format
result = json.dumps(food_titles)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
