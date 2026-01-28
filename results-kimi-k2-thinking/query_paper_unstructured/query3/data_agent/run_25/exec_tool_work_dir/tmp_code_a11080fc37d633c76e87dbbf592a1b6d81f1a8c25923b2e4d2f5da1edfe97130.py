code = """import json
import re

# Load data files
citation_file = locals()['var_functions.query_db:0']
papers_file = locals()['var_functions.query_db:2']

with open(citation_file, 'r') as f:
    citations = json.load(f)

with open(papers_file, 'r') as f:
    papers = json.load(f)

print('Loaded', len(citations), 'citations and', len(papers), 'papers')

# Build citation map with normalized titles
citation_lookup = {}
for c in citations:
    normalized = re.sub(r'[^a-zA-Z0-9]', '', c['title'].lower())
    citation_lookup[normalized] = int(c['total_citations'])

# Find empirical papers published after 2016 that have citation data
matched_results = []
matched_count = 0
empirical_after_2016_count = 0

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if filename and title:
        text = paper.get('text', '')
        
        # Extract years
        year_matches = re.findall(r'\b(20[0-2][0-9])\b', text)
        year = 0
        if year_matches:
            year = int(year_matches[0])
        
        # Check if empirical and after 2016
        has_empirical = 'empirical' in text.lower()
        
        if has_empirical and year > 2016:
            empirical_after_2016_count += 1
            
            # Normalize title for matching
            normalized_title = re.sub(r'[^a-zA-Z0-9]', '', title.lower())
            
            # Get citation count if exists
            citation_count = citation_lookup.get(normalized_title, 0)
            
            if citation_count > 0:
                matched_count += 1
                matched_results.append({
                    'title': title,
                    'year': year,
                    'total_citations': citation_count
                })

# Sort results by citation count
def get_citation(item):
    return item['total_citations']

matched_results.sort(key=get_citation, reverse=True)

# Print debug information
print('Empirical papers after 2016:', empirical_after_2016_count)
print('Papers matched with citations:', matched_count)

# Output final results
print('__RESULT__:')
print(json.dumps(matched_results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:34': [], 'var_functions.execute_python:38': [], 'var_functions.execute_python:42': []}

exec(code, env_args)
