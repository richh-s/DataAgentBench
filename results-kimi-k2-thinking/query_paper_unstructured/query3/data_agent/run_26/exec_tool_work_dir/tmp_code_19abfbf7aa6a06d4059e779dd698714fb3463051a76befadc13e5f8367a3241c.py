code = """import json
import re

# Load data
with open('file_storage/functions.query_db:2.json', 'r') as f:
    paper_docs = json.load(f)

with open('file_storage/functions.query_db:5.json', 'r') as f:
    citations = json.load(f)

# Extract paper information more carefully
papers = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Extract year (simple approach)
    year = None
    year_matches = re.findall(r'(19|20)\d{2}', text)
    if year_matches:
        # Take the most common year or the first one
        year = int(year_matches[0])
    
    # Check if empirical
    is_empirical = 'empirical' in text.lower()
    
    papers.append({
        'title': title,
        'year': year,
        'is_empirical': is_empirical
    })

# Filter and get citation counts
empirical_papers_after_2016 = [p for p in papers if p['is_empirical'] and p['year'] and p['year'] > 2016]

# Get total citations for each paper
citations_by_title = {}
for cit in citations:
    title = cit.get('title', '')
    count = int(cit.get('citation_count', 0))
    if title not in citations_by_title:
        citations_by_title[title] = 0
    citations_by_title[title] += count

# Add citation counts to filtered papers
for paper in empirical_papers_after_2016:
    paper['total_citations'] = citations_by_title.get(paper['title'], 0)

print('__RESULT__:')
print(json.dumps(empirical_papers_after_2016))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': {'paper_docs_type': "<class 'str'>", 'citations_type': "<class 'str'>", 'paper_docs_is_str': True, 'citations_is_str': True, 'paper_docs_preview': 'file_storage/functions.query_db:2.json', 'citations_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:16': {'paper_docs_loaded': 5, 'citations_loaded': 1405}}

exec(code, env_args)
