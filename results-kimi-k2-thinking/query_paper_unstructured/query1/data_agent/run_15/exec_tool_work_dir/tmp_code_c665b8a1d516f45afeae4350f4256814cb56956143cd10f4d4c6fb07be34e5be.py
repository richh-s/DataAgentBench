code = """import json
import re

# Read the stored result
result_file = var_functions.query_db:0
with open(result_file, 'r') as f:
    papers = json.load(f)

# Extract paper information
paper_info = []

for paper in papers:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Extract year from text (look for patterns like '2015', 'UBICOMP 2015', etc.)
    year_match = re.search(r'(\b20\d{2}\b)', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Extract venue (look for common venue patterns)
    venue_patterns = ['CHI', 'Ubicomp', 'CSCW', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH']
    venue = None
    for pattern in venue_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            venue = pattern
            break
    
    # Extract source/publisher
    source = None
    if 'ACM' in text:
        source = 'ACM'
    elif 'IEEE' in text:
        source = 'IEEE'
    elif 'PubMed' in text:
        source = 'PubMed'
    
    # Extract domain - look for 'food' specifically
    # Check if the paper mentions food domain
    domain = None
    # Look for domain indicators in the text
    if re.search(r'\bfood\b', text, re.IGNORECASE):
        domain = 'food'
    
    # Extract contribution type
    contribution = None
    contribution_patterns = {
        'empirical': ['empirical', 'study', 'survey', 'interview', 'questionnaire'],
        'artifact': ['system', 'tool', 'application', 'prototype', 'design'],
        'theoretical': ['model', 'theory', 'framework', 'conceptual'],
        'survey': ['survey', 'review', 'literature'],
        'methodological': ['method', 'methodology', 'approach']
    }
    
    for ctype, patterns in contribution_patterns.items():
        for pattern in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                if contribution is None:
                    contribution = ctype
                break
    
    if domain == 'food':  # Only include food domain papers
        paper_info.append({
            'title': title,
            'year': year,
            'venue': venue,
            'source': source,
            'domain': domain,
            'contribution': contribution
        })

print('__RESULT__:')
print(json.dumps(paper_info))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
