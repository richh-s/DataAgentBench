code = """import json
import re

# Load paper documents
paper_file = var_functions.query_db:2
with open(paper_file, 'r') as f:
    paper_docs = json.load(f)

# Load citations
citations_file = var_functions.query_db:1
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Extract paper metadata
papers = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename.endswith('.txt'):
        continue
    
    title = filename[:-4]
    
    # Extract year
    year_match = re.search(r'\b(2016)\b', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Check domain
    is_physical_activity = 'physical activity' in text.lower()
    
    if year == 2016 and is_physical_activity:
        papers.append(title)

# Aggregate citations by title
citation_counts = {}
for cit in citations:
    title = cit.get('title', '')
    if title in papers:
        count = int(cit.get('citation_count', 0))
        citation_counts[title] = citation_counts.get(title, 0) + count

# Format results
results = [{'title': title, 'total_citations': count} 
           for title, count in citation_counts.items()]

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
