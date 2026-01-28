code = """import json
import re

# Load the data from the stored file paths
with open('var_functions.query_db:1', 'r') as f:
    citations_data = json.load(f)

with open('var_functions.query_db:4', 'r') as f:
    paper_docs = json.load(f)

# Extract papers from 2016 in physical activity domain
papers_2016_pa = {}

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4]
    
    # Check if paper is from 2016
    year_match = re.search(r'\b(2016)\b', text)
    if not year_match:
        continue
    
    # Check if paper is in physical activity domain (case-insensitive)
    if 'physical activity' not in text.lower():
        continue
    
    papers_2016_pa[title] = {'year': 2016, 'domain': 'physical activity'}

# Calculate total citations for these papers
citation_totals = {}
for citation in citations_data:
    title = citation.get('title', '')
    if title in papers_2016_pa:
        try:
            count = int(citation.get('citation_count', 0))
            citation_totals[title] = citation_totals.get(title, 0) + count
        except (ValueError, TypeError):
            continue

# Format final results
results = []
for title in sorted(citation_totals.keys()):
    results.append({
        'title': title,
        'total_citations': citation_totals[title]
    })

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:26': {'query_vars': ['var_functions.query_db:0', 'var_functions.query_db:1', 'var_functions.query_db:4', 'var_functions.query_db:12'], 'all_vars_count': 6}}

exec(code, env_args)
