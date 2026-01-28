code = """import json
import re
from collections import defaultdict

# Load paper documents
paper_docs_path = locals()['var_functions.query_db:8']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Load citations
citations_path = locals()['var_functions.query_db:6']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Process citations to aggregate total citations per paper title
citation_totals = defaultdict(int)
for citation in citations:
    title = citation['title']
    count = int(citation['total_citations'])
    citation_totals[title] = count

# Process paper documents to extract metadata
papers = []
for doc in paper_docs:
    # Extract title from filename
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    text = doc.get('text', '')
    
    # Extract year - look for patterns like 2017, 2018, etc.
    year = None
    year_matches = re.findall(r'20[1-9][0-9]', text)
    if year_matches:
        # Get the smallest year (likely publication year)
        year = min(int(y) for y in year_matches)
    
    # Extract contribution - check if 'empirical' appears
    contribution = None
    if 'empirical' in text.lower():
        contribution = 'empirical'
    
    # Get total citations
    total_citations = citation_totals.get(title, 0)
    
    papers.append({
        'title': title,
        'year': year,
        'contribution': contribution,
        'total_citations': total_citations
    })

# Filter papers: empirical contribution AND published after 2016
filtered_results = []
for paper in papers:
    if paper['contribution'] == 'empirical' and paper['year'] and paper['year'] > 2016:
        filtered_results.append({
            'title': paper['title'],
            'total_citations': paper['total_citations']
        })

print('__RESULT__:')
print(json.dumps(filtered_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'paper_docs_count': 5, 'citations_count': 259}, 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'contribution': 'empirical', 'total_citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'contribution': 'empirical', 'total_citations': 266}]}

exec(code, env_args)
