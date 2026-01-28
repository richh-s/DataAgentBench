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
    
    # Extract year from text
    text = paper['text']
    year = None
    year_matches = re.findall(r"20[01][0-9]", text)
    if year_matches:
        # Take the smallest year that's >= 2000
        valid_years = [int(y) for y in year_matches if int(y) >= 2000]
        if valid_years:
            year = min(valid_years)
    
    # Check for empirical contribution
    text_lower = text.lower() if text else ""
    has_empirical = 'empirical' in text_lower or 'empirically' in text_lower
    
    extracted_papers.append({
        '_id': paper['_id'],
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

# Print results
result = {
    'extracted': extracted_papers,
    'count': len(extracted_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:14': {'paper_count': 5, 'citation_count': 1405}}

exec(code, env_args)
