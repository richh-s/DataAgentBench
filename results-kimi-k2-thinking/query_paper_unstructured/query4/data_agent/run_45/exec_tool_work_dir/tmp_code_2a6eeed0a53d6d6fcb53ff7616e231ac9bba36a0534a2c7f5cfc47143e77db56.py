code = """import json
import re

# Access data using string keys
citations_data = locals()['var_functions.query_db:1']
with open(citations_data, 'r') as f:
    citations = json.load(f)

paper_docs_path = locals()['var_functions.query_db:4']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Find papers from 2016 in physical activity domain
papers_2016_pa = {}
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4]
    
    if '2016' in text and 'physical activity' in text.lower():
        papers_2016_pa[title] = 0

# Calculate total citations for these papers
for citation in citations:
    title = citation.get('title', '')
    if title in papers_2016_pa:
        papers_2016_pa[title] += int(citation.get('citation_count', 0))

# Format results
results = [{'title': title, 'total_citations': count} 
           for title, count in papers_2016_pa.items() 
           if count > 0]

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:26': {'query_vars': ['var_functions.query_db:0', 'var_functions.query_db:1', 'var_functions.query_db:4', 'var_functions.query_db:12'], 'all_vars_count': 6}}

exec(code, env_args)
