code = """import json
import re

# Load paper documents
papers_file = locals()['var_functions.query_db:6']
with open(papers_file, 'r') as f:
    papers = json.load(f)

# Extract paper information
extracted_papers = []

for paper in papers:
    # Extract title from filename
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Extract year from text (looking for publication year patterns like '20XX')
    text = paper['text']
    year_match = re.search(r'\'([0-9]{2}),\s*(20[0-9]{2})', text)
    year = None
    if year_match:
        year = int(year_match.group(2))
    else:
        # Alternative patterns
        year_match = re.search(r'20[0-9]{2}', text)
        if year_match:
            year = int(year_match.group(0))
    
    # Check if contribution is empirical (look for 'empirical' in the text)
    contribution_types = []
    if text and 'empirical' in text.lower():
        contribution_types.append('empirical')
    
    # Also check for other indicators
    if text and 'empirically' in text.lower():
        contribution_types.append('empirical')
    
    extracted_papers.append({
        '_id': paper['_id'],
        'title': title,
        'year': year,
        'has_empirical': len(contribution_types) > 0
    })

print('__RESULT__:')
print(json.dumps(extracted_papers, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:14': {'paper_count': 5, 'citation_count': 1405}}

exec(code, env_args)
