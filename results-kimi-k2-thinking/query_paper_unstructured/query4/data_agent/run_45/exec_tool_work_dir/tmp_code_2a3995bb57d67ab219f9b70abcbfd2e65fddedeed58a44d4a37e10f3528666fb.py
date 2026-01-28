code = """import json
import re

# Get the file paths from locals
citations_path = var_functions.query_db:1
paper_docs_path = var_functions.query_db:4

# Load the data
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Process papers: find 2016 physical activity papers
papers_2016_pa = set()

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename.endswith('.txt'):
        continue
        
    title = filename[:-4]
    
    # Check year 2016
    if '2016' not in text:
        continue
        
    # Check physical activity domain
    if 'physical activity' not in text.lower():
        continue
        
    papers_2016_pa.add(title)

# Sum citations for these papers
citation_totals = {}
for citation in citations_data:
    title = citation.get('title', '')
    if title in papers_2016_pa:
        count = int(citation.get('citation_count', 0))
        citation_totals[title] = citation_totals.get(title, 0) + count

# Create results list
results = [
    {'title': title, 'total_citations': count}
    for title, count in citation_totals.items()
]

# Sort by title
results.sort(key=lambda x: x['title'])

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:26': {'query_vars': ['var_functions.query_db:0', 'var_functions.query_db:1', 'var_functions.query_db:4', 'var_functions.query_db:12'], 'all_vars_count': 6}}

exec(code, env_args)
