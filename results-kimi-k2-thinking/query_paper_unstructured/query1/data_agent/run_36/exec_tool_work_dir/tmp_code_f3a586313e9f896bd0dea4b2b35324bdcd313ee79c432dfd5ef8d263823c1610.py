code = """import json
import re

# Read the result file
result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    papers_data = json.load(f)

print(f"Total papers retrieved: {len(papers_data)}")

# Process papers to identify those in food domain
food_papers = []
for paper in papers_data:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    
    # Look for food-related patterns in the text
    # According to the hints, we should use substring matching
    # Common domains include: "food", "physical activity", "sleep", "mental", etc.
    if 'food' in text:
        # Extract title from filename (without .txt extension)
        title = filename.replace('.txt', '')
        food_papers.append({
            'title': title,
            'filename': filename,
            '_id': paper.get('_id')
        })

print(f"Food-related papers found: {len(food_papers)}")
print("First few food papers:", food_papers[:5])

# Convert to JSON for the next step
import json as js
result = js.dumps(food_papers)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
