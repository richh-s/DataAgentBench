code = """import json
import re

# Load paper documents
papers_path = locals()['var_functions.query_db:26']
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Debug: Check for empirical papers
empirical_papers = []
for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    
    if 'empirical' in text:
        # Extract year from this paper
        year_match = re.search(r'\b(201[0-9]|202[0-9])\b', paper.get('text', ''))
        year = year_match.group(1) if year_match else 'Unknown'
        
        empirical_papers.append({
            'title': filename.replace('.txt', ''),
            'year': year,
            'has_empirical': True
        })

# Debug: Check all papers for year patterns
years_found = []
for paper in papers:
    text = paper.get('text', '')
    matches = re.findall(r'\b(201[0-9]|202[0-9])\b', text)
    if matches:
        years_found.extend(matches)

# Show some full text samples with years
samples = []
for i, paper in enumerate(papers[:3]):
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Find all year patterns in this paper
    year_matches = re.findall(r'\b(201[0-9]|202[0-9])\b', text)
    
    # Get first 500 chars to preview
    preview = text[:500]
    
    samples.append({
        'filename': filename,
        'years_found': year_matches,
        'preview': preview,
        'has_empirical': 'empirical' in text.lower()
    })

result = {
    'empirical_papers_found': len(empirical_papers),
    'empirical_papers': empirical_papers[:5],
    'all_years_found': list(set(years_found)),
    'samples': samples
}

import json as js
print('__RESULT__:')
print(js.dumps(result, ensure_ascii=False, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'paper_count': 38, 'citation_count': 38}, 'var_functions.execute_python:22': {'paper_type': "<class 'str'>", 'paper_len': 38, 'citation_type': "<class 'str'>", 'citation_len': 38}, 'var_functions.execute_python:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json', 'var_functions.execute_python:30': [], 'var_functions.execute_python:34': []}

exec(code, env_args)
