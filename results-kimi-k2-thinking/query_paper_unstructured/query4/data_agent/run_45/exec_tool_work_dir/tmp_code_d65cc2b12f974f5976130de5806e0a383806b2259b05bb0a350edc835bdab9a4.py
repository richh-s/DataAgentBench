code = """import json
import re

# Read paper documents from file
paper_docs_file = var_functions.query_db:12
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Read citations from file
citations_file = var_functions.query_db:1
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Process papers to find those from 2016 in physical activity domain
papers_2016_physical_activity = {}

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    # Check if paper is from 2016
    year_match = re.search(r'\b(2016)\b', text)
    if not year_match:
        continue
    
    # Check if paper is in physical activity domain
    if 'physical activity' not in text.lower():
        continue
    
    papers_2016_physical_activity[title] = title

# Calculate total citations for these papers
citation_totals = {}
for citation in citations_data:
    title = citation.get('title', '')
    if title in papers_2016_physical_activity:
        count = int(citation.get('citation_count', 0))
        citation_totals[title] = citation_totals.get(title, 0) + count

# Format results
results = []
for title, total_citations in citation_totals.items():
    results.append({
        'title': title,
        'total_citations': total_citations
    })

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
