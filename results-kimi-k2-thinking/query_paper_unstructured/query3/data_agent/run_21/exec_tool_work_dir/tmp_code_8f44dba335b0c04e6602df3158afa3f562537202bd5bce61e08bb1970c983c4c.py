code = """import json
import re

# Read the JSON file containing MongoDB results
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

# Function to extract paper information from text
extracted_papers = []

for doc in paper_docs:
    try:
        filename = doc['filename']
        # Extract title from filename
        title = filename.replace('.txt', '')
        
        text = doc.get('text', '')
        
        # Extract year - look for 4-digit years in 2017-2029 range
        year_match = re.search(r'20(1[7-9]|2[0-9])', text)
        year = int(year_match.group()) if year_match else None
        
        # Extract contribution type - search for empirical keyword
        contribution = None
        if 'empirical' in text.lower():
            contribution = 'empirical'
        
        # Get venue, source, domain if present (for validation, not needed for query)
        venue_match = re.search(r'\b(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UBICOMP)\b', text, re.IGNORECASE)
        venue = venue_match.group(0).upper() if venue_match else None
        
        source_match = re.search(r'\b(ACM|IEEE|PubMed)\b', text, re.IGNORECASE)
        source = source_match.group(0) if source_match else None
        
        # Only include papers with valid year, title and empirical contribution
        if title and year and contribution == 'empirical':
            extracted_papers.append({
                'title': title,
                'year': year
            })
    except Exception as e:
        # Skip documents with errors
        continue

# Filter for papers published after 2016
empirical_papers_after_2016 = [p for p in extracted_papers if p['year'] > 2016]

print('__RESULT__:')
print(json.dumps(empirical_papers_after_2016))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
