code = """import json

# Read the full query result
with open('functions_query_db_2.json', 'r') as f:
    food_papers = json.load(f)

print(f"Found {len(food_papers)} papers mentioning 'food'")

# Extract titles from filenames (remove .txt extension)
food_titles = []
for paper in food_papers:
    filename = paper.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]  # Remove .txt
        food_titles.append(title)

print(f"Extracted {len(food_titles)} titles")
print(f"Sample titles: {food_titles[:5]}")

# Print result in required format
result = json.dumps(food_titles)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
