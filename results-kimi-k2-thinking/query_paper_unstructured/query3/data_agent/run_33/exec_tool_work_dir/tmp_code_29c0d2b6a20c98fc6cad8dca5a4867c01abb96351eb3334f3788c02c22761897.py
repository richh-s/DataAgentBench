code = """import json
import re

# Load paper documents
paper_docs_path = var_functions.query_db:0
paper_docs = json.load(open(paper_docs_path))

print(f'Loaded {len(paper_docs)} papers')

# Extract info from papers
papers_info = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else 'Unknown'
    
    # Extract year
    year = None
    year_match = re.search(r'(20\d{2})', text)
    if year_match:
        year = int(year_match.group(1))
    else:
        # Try 2-digit year format (UBICOMP '15, CHI '16, etc.)
        year_match = re.search(r"(UBICOMP|CHI|CSCW|DIS)\s*\'(\d{2})", text)
        if year_match:
            year_str = year_match.group(2)
            year = int('20' + year_str) if int(year_str) < 50 else int('19' + year_str)
    
    # Extract contribution
    contribution = None
    if 'empirical' in text.lower():
        contribution = 'empirical'
    elif 'artifact' in text.lower():
        contribution = 'artifact'
    elif 'theoretical' in text.lower():
        contribution = 'theoretical'
    elif 'survey' in text.lower():
        contribution = 'survey'
    elif 'methodological' in text.lower():
        contribution = 'methodological'
    
    papers_info.append({'title': title, 'year': year, 'contribution': contribution})

# Filter empirical papers after 2016
filtered = [p for p in papers_info if p['contribution'] == 'empirical' and p['year'] and p['year'] > 2016]

print(f'Found {len(filtered)} empirical papers after 2016')
for p in filtered:
    print(f"  - {p['title']} ({p['year']})")

# Prepare result
result = {'papers': filtered}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'paper_docs_count': 5, 'citations_count': 1405}}

exec(code, env_args)
