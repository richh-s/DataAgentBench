code = """import json
import re

# Load data
with open('file_storage/functions.query_db:2.json', 'r') as f:
    paper_docs = json.load(f)

with open('file_storage/functions.query_db:5.json', 'r') as f:
    citations = json.load(f)

# Extract paper information
papers = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = re.sub(r'\.txt$', '', filename)
    
    # Try to extract year from text (look for patterns like '2015', 'SEPTEMBER 7-11, 2015', etc.)
    year_match = re.search(r'(19|20)\d{2}', text)
    year = int(year_match.group()) if year_match else None
    
    # Check if it's empirical (case-insensitive search)
    is_empirical = bool(re.search(r'\bempirical\b', text, re.IGNORECASE))
    
    # Extract contribution type (look for common patterns)
    contribution = None
    if re.search(r'\bempirical\b', text, re.IGNORECASE):
        contribution = 'empirical'
    elif re.search(r'\btheoretical\b', text, re.IGNORECASE):
        contribution = 'theoretical'
    elif re.search(r'\bartifact\b', text, re.IGNORECASE):
        contribution = 'artifact'
    elif re.search(r'\bsurvey\b', text, re.IGNORECASE):
        contribution = 'survey'
    
    # Extract venue (look for common HCI venues)
    venue = None
    venue_patterns = [
        r'CHI\s*\'?\d{2}', r'Ubicomp|UbiComp', r'CSCW', r'DIS', r'PervasiveHealth',
        r'WWW', r'IUI', r'OzCHI', r'TEI', r'AH', r'UIST', r'ISS', r'MobileHCI'
    ]
    
    for pattern in venue_patterns:
        if re.search(pattern, text):
            # Extract just the venue name
            if 'CHI' in pattern:
                venue = 'CHI'
            elif 'Ubicomp' in pattern or 'UbiComp' in pattern:
                venue = 'Ubicomp'
            elif 'CSCW' in pattern:
                venue = 'CSCW'
            elif 'DIS' in pattern:
                venue = 'DIS'
            elif 'PervasiveHealth' in pattern:
                venue = 'PervasiveHealth'
            elif 'WWW' in pattern:
                venue = 'WWW'
            elif 'IUI' in pattern:
                venue = 'IUI'
            elif 'OzCHI' in pattern:
                venue = 'OzCHI'
            elif 'TEI' in pattern:
                venue = 'TEI'
            elif 'AH' in pattern:
                venue = 'AH'
            break
    
    papers.append({
        'title': title,
        'year': year,
        'venue': venue,
        'contribution': contribution,
        'is_empirical': is_empirical
    })

# Filter empirical papers published after 2016
empirical_papers_after_2016 = [
    p for p in papers 
    if p['is_empirical'] and p['year'] and p['year'] > 2016
]

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(papers),
    'empirical_papers': len([p for p in papers if p['is_empirical']]),
    'empirical_after_2016': len(empirical_papers_after_2016),
    'papers': papers,
    'filtered_papers': empirical_papers_after_2016
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'paper_docs_type': "<class 'str'>", 'citations_type': "<class 'str'>", 'paper_docs_is_str': True, 'citations_is_str': True, 'paper_docs_preview': 'file_storage/functions.query_db:2.json', 'citations_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:16': {'paper_docs_loaded': 5, 'citations_loaded': 1405}}

exec(code, env_args)
