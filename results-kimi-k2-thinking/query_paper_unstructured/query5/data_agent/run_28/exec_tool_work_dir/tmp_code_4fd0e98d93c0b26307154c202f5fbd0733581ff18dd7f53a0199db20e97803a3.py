code = """import json
import re

# Load the datasets
citations_file = var_functions.query_db:0
papers_file = var_functions.query_db:6

with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Find CHI paper titles
chi_titles = set()
for paper in paper_docs:
    title = paper['filename'].replace('.txt', '')
    text = paper.get('text', '')
    # Check if CHI appears in filename or text
    if 'CHI' in text or 'chi' in paper['filename'].lower():
        chi_titles.add(title)

# Sum citations for CHI papers in 2020
total_citations = 0
matching_papers = []

for citation in citations_2020:
    title = citation['title']
    if title in chi_titles:
        count = int(citation['citation_count'])
        total_citations += count
        matching_papers.append({
            'title': title,
            'citations_2020': count
        })

# Prepare result
result = {
    'total_chi_papers': len(matching_papers),
    'total_citations_2020': total_citations,
    'paper_details': matching_papers
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:30': {'citations_type': "<class 'str'>", 'citations_preview': 'file_storage/functions.query_db:0.json', 'papers_type': "<class 'str'>", 'papers_preview': 'file_storage/functions.query_db:6.json'}}

exec(code, env_args)
