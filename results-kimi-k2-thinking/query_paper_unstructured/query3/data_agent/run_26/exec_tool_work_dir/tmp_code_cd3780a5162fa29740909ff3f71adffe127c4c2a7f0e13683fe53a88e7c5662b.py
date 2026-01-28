code = """import json
import re

# Load data
with open('file_storage/functions.query_db:2.json', 'r') as f:
    paper_docs = json.load(f)

with open('file_storage/functions.query_db:5.json', 'r') as f:
    citations = json.load(f)

# Extract paper information with correct year parsing
papers = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    title = filename.replace('.txt', '')
    
    # Extract year correctly
    year = None
    year_match = re.search(r'(19|20)\d{2}', text)
    if year_match:
        year = int(year_match.group())
    
    # Check for empirical contribution
    is_empirical = 'empirical' in text.lower()
    
    papers.append({
        'title': title,
        'year': year,
        'is_empirical': is_empirical
    })

# Build citation map
citations_by_title = {}
for cit in citations:
    title = cit.get('title', '')
    count = int(cit.get('citation_count', 0))
    if title not in citations_by_title:
        citations_by_title[title] = 0
    citations_by_title[title] += count

# Find empirical papers after 2016
empirical_after_2016 = []
for paper in papers:
    if paper['is_empirical'] and paper['year'] and paper['year'] > 2016:
        title = paper['title']
        total_citations = citations_by_title.get(title, 0)
        empirical_after_2016.append({
            'title': title,
            'year': paper['year'],
            'total_citations': total_citations
        })

# Sort by citations descending
empirical_after_2016.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'papers_processed': papers,
    'empirical_after_2016': empirical_after_2016
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'paper_docs_type': "<class 'str'>", 'citations_type': "<class 'str'>", 'paper_docs_is_str': True, 'citations_is_str': True, 'paper_docs_preview': 'file_storage/functions.query_db:2.json', 'citations_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:16': {'paper_docs_loaded': 5, 'citations_loaded': 1405}, 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': {'total_papers': 5, 'papers_with_year': 5, 'year_distribution': {'20': 5}, 'empirical_papers': 2, 'empirical_by_year': {'20': 2}, 'empirical_after_2016': 0, 'empirical_after_2016_list': [], 'total_citations_found': 5}}

exec(code, env_args)
