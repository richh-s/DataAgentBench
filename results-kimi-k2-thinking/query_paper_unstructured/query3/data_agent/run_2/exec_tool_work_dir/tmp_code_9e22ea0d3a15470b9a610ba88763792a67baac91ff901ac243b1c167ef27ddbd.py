code = """import json

# Get file paths
paper_docs_path = locals()['var_functions.query_db:2']
citations_path = locals()['var_functions.query_db:5']

# Read actual data from files
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

with open(citations_path, 'r') as f:
    citations = json.load(f)

# Process and extract needed information
import re
from collections import defaultdict

# Extract paper info
papers_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Extract year
    year_match = re.search(r'(20[0-2][0-9])', text[:2000])
    year = int(year_match.group(1)) if year_match else None
    
    # Check for empirical contribution
    text_lower = text.lower()
    has_empirical = bool(re.search(r'empirical|study|survey|interview|experiment|evaluation', text_lower))
    
    if title:
        papers_info.append({
            'title': title,
            'year': year,
            'empirical': has_empirical
        })

# Group citations by title
citations_by_title = defaultdict(int)
for citation in citations:
    cit_title = citation.get('title', '').lower()
    cit_count = int(citation.get('citation_count', 0))
    citations_by_title[cit_title] += cit_count

# Filter and get results
result = []
for paper in papers_info:
    if paper['year'] and paper['year'] > 2016 and paper['empirical']:
        title = paper['title']
        total_citations = citations_by_title.get(title.lower(), 0)
        result.append({
            'title': title,
            'total_citations': total_citations
        })

# Sort by citations
result.sort(key=lambda x: x['total_citations'], reverse=True)

# Print in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:16': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 0}]}

exec(code, env_args)
