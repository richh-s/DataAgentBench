code = """import json
import re

# Load data
citation_path = locals()['var_functions.query_db:0']
mongodb_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(mongodb_path, 'r') as f:
    papers = json.load(f)

# Create citation map (normalized titles to counts)
citation_map = {}
for c in citations:
    norm_title = re.sub(r'[^a-zA-Z0-9]', '', c['title'].lower())
    citation_map[norm_title] = int(c['total_citations'])

# Find matching empirical papers published after 2016
results = []

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if title:
        text = paper.get('text', '')
        years = re.findall(r'\b(20[0-2][0-9])\b', text)
        year = int(years[0]) if years else 0
        
        has_empirical = 'empirical' in text.lower()
        
        if year > 2016 and has_empirical:
            norm_title = re.sub(r'[^a-zA-Z0-9]', '', title.lower())
            citation_count = citation_map.get(norm_title, 0)
            
            if citation_count > 0:
                results.append({
                    'title': title,
                    'year': year,
                    'total_citations': citation_count
                })

# Sort by citations descending
def sort_key(item):
    return item['total_citations']

results.sort(key=sort_key, reverse=True)

# Output
output = json.dumps(results)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:34': [], 'var_functions.execute_python:38': []}

exec(code, env_args)
