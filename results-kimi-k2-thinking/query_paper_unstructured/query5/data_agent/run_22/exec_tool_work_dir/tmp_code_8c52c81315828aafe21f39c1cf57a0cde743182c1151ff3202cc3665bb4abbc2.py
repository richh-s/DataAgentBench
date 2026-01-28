code = """import json
import pandas as pd
import re

# Get data from storage
citations_data = locals()['var_functions.query_db:5']
paper_docs_data = locals()['var_functions.query_db:6']

print(type(citations_data))
print(type(paper_docs_data))

# Check if these are file paths or actual data
if isinstance(citations_data, str) and citations_data.endswith('.json'):
    # It's a file path
    with open(citations_data, 'r') as f:
        citations_data = json.load(f)

if isinstance(paper_docs_data, str) and paper_docs_data.endswith('.json'):
    # It's a file path
    with open(paper_docs_data, 'r') as f:
        paper_docs_data = json.load(f)

print(f"Citations records: {len(citations_data)}")
print(f"Paper docs records: {len(paper_docs_data)}")

# Find CHI papers in the documents
chi_paper_titles = []
for paper in paper_docs_data:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    # Check if CHI appears in the text (common indicator of CHI venue)
    if re.search(r'\\bCHI\\b', text, re.IGNORECASE):
        title = filename.replace('.txt', '') if filename else ''
        chi_paper_titles.append(title)

print(f"Found {len(chi_paper_titles)} CHI papers")

# Create a set for fast lookup
chi_titles_set = set([t.lower() for t in chi_paper_titles])

# Match with citations data and sum up citations for 2020
total_citations = 0
chi_citations_list = []

for citation in citations_data:
    cite_title = citation.get('title', '').lower()
    if cite_title in chi_titles_set:
        count = int(citation.get('citation_count', 0))
        total_citations += count
        original_title = next(t for t in chi_paper_titles if t.lower() == cite_title)
        chi_citations_list.append({
            'title': original_title,
            'citation_count': count
        })

# Sort by citation count
chi_citations_list.sort(key=lambda x: x['citation_count'], reverse=True)

result = {
    'total_citations': total_citations,
    'num_papers': len(chi_citations_list),
    'papers': chi_citations_list
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
