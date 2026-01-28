code = """import json
import re

# Access the variable from storage
result_path = locals()['var_functions.query_db:2']

# Read the result file
with open(result_path, 'r') as f:
    papers_data = json.load(f)

print(f"Total papers retrieved: {len(papers_data)}")

# Process papers to identify those in food domain
food_papers = []
for paper in papers_data:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    
    # Look for food-related patterns in the text
    if 'food' in text:
        # Extract title from filename (without .txt extension)
        title = filename.replace('.txt', '')
        food_papers.append({
            'title': title,
            'filename': filename,
            '_id': paper.get('_id')
        })

print(f"Food-related papers found: {len(food_papers)}")

# Convert to JSON
result_json = json.dumps(food_papers)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
