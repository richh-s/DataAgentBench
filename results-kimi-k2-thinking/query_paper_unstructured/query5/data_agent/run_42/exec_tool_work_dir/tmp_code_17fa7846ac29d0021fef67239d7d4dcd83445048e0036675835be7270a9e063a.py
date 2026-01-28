code = """import json
import os
import re

# Load the data
citations_key = 'var_functions.query_db:0'
citations_file = locals()[citations_key]
if isinstance(citations_file, str) and os.path.exists(citations_file):
    with open(citations_file, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_file

papers_key = 'var_functions.query_db:6'
papers_file = locals()[papers_key]
if isinstance(papers_file, str) and os.path.exists(papers_file):
    with open(papers_file, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = papers_file

# Create a mapping from paper titles to their venue information
paper_venues = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = re.sub(r'\.txt$', '', filename)
    
    # Look for CHI venue information in the text
    # Common patterns: CHI, CHI Conference, CHI 'year, CHI year, etc.
    chi_patterns = [
        r'CHI\s+\'?\d{2}',  # CHI '15, CHI 15
        r'CHI\s+\d{4}',    # CHI 2015
        r'CHI\s+Conference',  # CHI Conference
        r'Proceedings\s+of\s+CHI',  # Proceedings of CHI
        r'CHI\s+\d{2,4}\s*,',  # CHI year,
    ]
    
    is_chi = False
    for pattern in chi_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            is_chi = True
            break
    
    if is_chi and title:
        paper_venues[title] = 'CHI'

print(f'Found {len(paper_venues)} papers from CHI venue')
print('__RESULT__:')
print(json.dumps(f'Found {len(paper_venues)} CHI papers'))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 188, 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Data loaded successfully'}

exec(code, env_args)
