code = """import json
import re

citation_path = locals()['var_functions.query_db:0']
mongodb_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(mongodb_path, 'r') as f:
    papers = json.load(f)

# Total counts
print('Total citations: ' + str(len(citations)))
print('Total papers: ' + str(len(papers)))

# Extract paper information
papers_with_empirical = []

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    # Extract year - try multiple patterns
    year = None
    # Four digit year pattern
    match = re.search(r'\b(201[7-9]|202[0-9])\b', text)
    if match:
        year = int(match.group(1))
    
    # Check for empirical contribution
    empirical = 'empirical' in text.lower()
    
    if title and year and empirical:
        papers_with_empirical.append({'title': title, 'year': year})

print('Papers empirical and after 2016: ' + str(len(papers_with_empirical)))

# Get citation dictionary
citation_dict = {}
for c in citations:
    citation_dict[c['title']] = int(c['total_citations'])

# Join with citation data
results = []
for paper in papers_with_empirical:
    title = paper['title']
    if title in citation_dict:
        results.append({
            'title': title,
            'year': paper['year'],
            'total_citations': citation_dict[title]
        })

# Sort by citation count
def sort_key(item):
    return item['total_citations']

results.sort(key=sort_key, reverse=True)

# Format output
output = json.dumps(results, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': []}

exec(code, env_args)
