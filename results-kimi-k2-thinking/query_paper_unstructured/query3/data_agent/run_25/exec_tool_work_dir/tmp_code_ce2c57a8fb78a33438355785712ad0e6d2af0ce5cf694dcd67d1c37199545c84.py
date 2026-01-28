code = """import json
import re

# Load data
citation_path = locals()['var_functions.query_db:0']
mongodb_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(mongodb_path, 'r') as f:
    papers = json.load(f)

# Create clean title mappings
citation_map = {}
for c in citations:
    title = c['title'].strip()
    # Create normalized key
    normalized = re.sub(r'[^a-zA-Z0-9]', '', title.lower())
    citation_map[normalized] = int(c['total_citations'])

# Process papers
results = []

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    if not title:
        continue
    
    # Extract year
    years = re.findall(r'\b(20[0-2][0-9])\b', text)
    year = int(years[0]) if years else 0
    
    # Check for empirical
    has_empirical = 'empirical' in text.lower()
    
    # Check if published after 2016
    if year > 2016 and has_empirical:
        # Normalize title to match
        normalized_title = re.sub(r'[^a-zA-Z0-9]', '', title.lower())
        
        # Find citation count
        total_citations = citation_map.get(normalized_title, 0)
        
        if total_citations > 0:
            results.append({
                'title': title,
                'year': year,
                'total_citations': total_citations
            })

# Sort by citation count
def get_citations(item):
    return item['total_citations']

results.sort(key=get_citations, reverse=True)

# Print summary
print('Total empirical papers after 2016: ' + str(len([p for p in papers if 'empirical' in p.get('text', '').lower() and re.search(r'\b(20[1-9][0-9])\b', p.get('text', '')) ])))
print('Total papers matched with citations: ' + str(len(results)))

# Output
print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': []}

exec(code, env_args)
