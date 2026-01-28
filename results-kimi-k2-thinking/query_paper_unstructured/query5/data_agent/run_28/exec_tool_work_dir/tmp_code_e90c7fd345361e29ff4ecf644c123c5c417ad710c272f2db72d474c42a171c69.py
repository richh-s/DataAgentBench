code = """import json
import re

# Access storage variables with string keys since they contain colons
storage = locals()
citations_file = storage['var_functions.query_db:0']
papers_file = storage['var_functions.query_db:6']

# Load data from file paths
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Identify CHI papers from the document collection
chi_paper_titles = set()
for paper in paper_docs:
    title = paper['filename'].replace('.txt', '')
    text = paper.get('text', '')
    # Check if it's a CHI paper
    if 'CHI' in text or 'CHI' in paper['filename']:
        chi_paper_titles.add(title)

# Calculate total citations for CHI papers in 2020
chi_papers_cited = []
total_citations = 0

for citation in citations_2020:
    title = citation['title']
    if title in chi_paper_titles:
        count = int(citation['citation_count'])
        total_citations += count
        chi_papers_cited.append({
            'title': title,
            'citations_in_2020': count
        })

# Return result in required format
result = {
    'total_chi_papers_analyzed': len(chi_papers_cited),
    'total_citations_in_2020': total_citations,
    'papers': chi_papers_cited
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:30': {'citations_type': "<class 'str'>", 'citations_preview': 'file_storage/functions.query_db:0.json', 'papers_type': "<class 'str'>", 'papers_preview': 'file_storage/functions.query_db:6.json'}}

exec(code, env_args)
