code = """import json
import re

# Read the full MongoDB query result from file
with open('file_storage/functions.query_db:2.json', 'r') as f:
    papers = json.load(f)

# Extract relevant information: title, year, domain
papers_2016_physical_activity = []

for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year - look for patterns like '2016' in the text
    # Common patterns: year in headers, references, etc.
    year_match = re.search(r'2016', text)
    year = 2016 if year_match else None
    
    # Check if domain contains 'physical activity'
    # Look for 'physical activity' in the text (case-insensitive)
    if re.search(r'physical activity', text, re.IGNORECASE):
        domain = 'physical activity'
    else:
        domain = None
    
    # Only include papers from 2016 in physical activity domain
    if year == 2016 and domain == 'physical activity':
        papers_2016_physical_activity.append({
            'title': title,
            'year': year,
            'domain': domain
        })

# Print result in required format
print('__RESULT__:')
print(json.dumps(papers_2016_physical_activity))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': ['functions.query_db:2.json']}

exec(code, env_args)
