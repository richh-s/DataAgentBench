code = """import json
import re

# Load data from files
citation_path = locals()['var_functions.query_db:0']
mongodb_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(mongodb_path, 'r') as f:
    papers = json.load(f)

# Build citation dictionary with normalized titles
citation_dict = {}
for citation in citations:
    # Normalize title for matching (remove punctuation, lowercase)
    norm_title = re.sub(r'[^a-zA-Z0-9]', '', citation['title'].lower())
    citation_dict[norm_title] = int(citation['total_citations'])

# Process papers to find empirical papers published after 2016
results = []

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not title:
        continue
    
    text = paper.get('text', '')
    
    # Extract publication year
    years = re.findall(r'\b(20[0-2][0-9])\b', text)
    year = int(years[0]) if years else 0
    
    # Check for empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    # Only include papers after 2016 with empirical contribution
    if year > 2016 and has_empirical:
        # Normalize paper title for matching
        norm_paper_title = re.sub(r'[^a-zA-Z0-9]', '', title.lower())
        
        # Get citation count if available
        total_citations = citation_dict.get(norm_paper_title, 0)
        
        if total_citations > 0:
            results.append({
                'title': title,
                'year': year,
                'total_citations': total_citations
            })

# Sort by total citations descending
results.sort(key=lambda x: x['total_citations'], reverse=True)

# Output as JSON
print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:34': []}

exec(code, env_args)
