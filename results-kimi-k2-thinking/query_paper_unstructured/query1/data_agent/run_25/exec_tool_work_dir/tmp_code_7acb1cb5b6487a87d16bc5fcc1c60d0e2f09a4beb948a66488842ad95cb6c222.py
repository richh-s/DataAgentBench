code = """import json

# Get the result from storage using locals() to handle the colon in variable name
storage_key = 'var_functions.query_db:2'
food_papers_data = locals()[storage_key]

# Check if it's a file path (string) or actual data
if isinstance(food_papers_data, str):
    # It's a file path, read the file
    with open(food_papers_data, 'r') as f:
        food_papers = json.load(f)
else:
    # It's already the data
    food_papers = food_papers_data

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
