code = """import json
import re

# Load paper documents
paper_docs_path = locals()['var_functions.query_db:8']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Load citations
citations_path = locals()['var_functions.query_db:6']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Create a dictionary of total citations per paper title for easy lookup
citation_dict = {item['title']: int(item['total_citations']) for item in citations}

# Extract paper information
papers = []
for doc in paper_docs:
    # Extract title from filename
    title = doc['filename'].replace('.txt', '')
    text = doc['text']
    
    # Extract year - look for year patterns (4 digits) in text
    # Common patterns: '17, 2017, CHI '18, etc.
    year_match = re.search(r'(\D|^)(20[1-9][0-9])(\D|$)', text)
    year = None
    if year_match:
        year = int(year_match.group(2))
    
    # Extract contribution - check if 'empirical' appears in text
    contribution = None
    if 'empirical' in text.lower():
        contribution = 'empirical'
    
    papers.append({
        'title': title,
        'year': year,
        'contribution': contribution,
        'total_citations': citation_dict.get(title, 0)
    })

# Filter papers: empirical contribution AND year > 2016
filtered_papers = []
for paper in papers:
    if paper['contribution'] == 'empirical' and paper['year'] and paper['year'] > 2016:
        filtered_papers.append(paper)

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'paper_docs_count': 5, 'citations_count': 259}}

exec(code, env_args)
