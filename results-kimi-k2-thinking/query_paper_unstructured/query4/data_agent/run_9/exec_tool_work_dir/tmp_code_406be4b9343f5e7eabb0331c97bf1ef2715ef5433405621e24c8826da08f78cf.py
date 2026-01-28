code = """import json
import pandas as pd

# Let's read the results from the previous query
result_path = var_functions.query_db:8  # This is the file path
with open(result_path, 'r') as f:
    papers = json.load(f)

print(f"Found {len(papers)} papers mentioning 'physical activity'")

# Filter papers from 2016
papers_2016 = []
for paper in papers:
    # Extract title from filename
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else 'Unknown'
    
    text = paper.get('text', '').lower()
    
    # Check if it's from 2016
    has_2016 = '2016' in paper.get('text', '')
    
    # Check if it mentions physical activity
    has_physical_activity = 'physical activity' in text
    
    if has_2016 and has_physical_activity:
        papers_2016.append({
            'title': title,
            'filename': filename
        })

print(f"Found {len(papers_2016)} papers from 2016 mentioning physical activity")
for p in papers_2016:
    print(f"  - {p['title']}")

# Export results for next step
print('__RESULT__:')
print(json.dumps(papers_2016))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
