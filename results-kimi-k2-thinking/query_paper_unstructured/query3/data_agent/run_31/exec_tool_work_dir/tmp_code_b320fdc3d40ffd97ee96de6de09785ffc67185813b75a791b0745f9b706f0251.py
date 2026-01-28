code = """import json
import re

# The query result is a file path string
file_path = locals()['var_functions.query_db:4']

# Read the JSON file
with open(file_path, 'r') as f:
    papers_data = json.load(f)

# Extract paper information from the documents
papers_info = []

for doc in papers_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Extract year from the text - look for 4-digit years starting with 20
    year_match = re.search(r"\b(20\d{2})\b", text[:2000])
    if year_match:
        year = int(year_match.group(1))
    else:
        # Look for venue pattern
        venue_year_match = re.search(r"(CHI|CSCW|Ubicomp|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*['\s]\s*(20\d{2})", text[:2000], re.IGNORECASE)
        if venue_year_match:
            year = int(venue_year_match.group(2))
        else:
            year = None
    
    # Extract contribution type from the text
    contribution = []
    text_lower = text.lower()
    
    # Check for empirical contribution indicators
    if 'empirical' in text_lower or 'study' in text_lower or 'survey' in text_lower or 'interview' in text_lower or 'experiment' in text_lower or 'user study' in text_lower:
        contribution.append('empirical')
    
    # Check for theoretical contribution
    if 'theoretical' in text_lower or 'theory' in text_lower:
        contribution.append('theoretical')
    
    # Check for artifact contribution
    if 'artifact' in text_lower or 'system' in text_lower or 'prototype' in text_lower or 'design' in text_lower:
        contribution.append('artifact')
    
    # Check for methodological contribution
    if 'methodological' in text_lower or 'method' in text_lower or 'framework' in text_lower or 'model' in text_lower:
        contribution.append('methodological')
    
    papers_info.append({
        'title': title,
        'year': year,
        'contribution': ','.join(contribution) if contribution else 'unknown'
    })

# Show the extracted papers
print('__RESULT__:')
print(json.dumps(papers_info, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': "<class 'str'>", 'var_functions.execute_python:14': 'Loaded 5 papers'}

exec(code, env_args)
