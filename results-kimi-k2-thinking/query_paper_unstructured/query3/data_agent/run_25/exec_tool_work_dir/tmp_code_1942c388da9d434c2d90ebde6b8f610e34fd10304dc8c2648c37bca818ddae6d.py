code = """import json
import re

# Load data files
citation_path = locals()['var_functions.query_db:0']
mongodb_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(mongodb_path, 'r') as f:
    papers = json.load(f)

# Verify data loaded
print('Loaded citations count: ' + str(len(citations)))
print('Loaded papers count: ' + str(len(papers)))

# Build normalized citation map for matching
citation_map = {}
for c in citations:
    norm_title = re.sub(r'[^a-zA-Z0-9]', '', c['title'].lower())
    citation_map[norm_title] = int(c['total_citations'])

# Find empirical papers published after 2016
empirical_papers = []

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not title:
        continue
    
    text = paper.get('text', '')
    
    # Extract year
    years = re.findall(r'\b(20[0-2][0-9])\b', text)
    year = int(years[0]) if years else 0
    
    # Check for empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    if year > 2016 and has_empirical:
        empirical_papers.append({'title': title, 'year': year})

print('Empirical papers after 2016: ' + str(len(empirical_papers)))

# Match with citation data using normalized titles
matched_papers = []

for paper in empirical_papers:
    norm_title = re.sub(r'[^a-zA-Z0-9]', '', paper['title'].lower())
    citation_count = citation_map.get(norm_title, 0)
    
    if citation_count > 0:
        paper_with_citations = {
            'title': paper['title'],
            'year': paper['year'],
            'total_citations': citation_count
        }
        matched_papers.append(paper_with_citations)

# Sort by citation count descending
def sort_by_citations(item):
    return item['total_citations']

matched_papers.sort(key=sort_by_citations, reverse=True)

# Output results
print('Matched papers with citations: ' + str(len(matched_papers)))

if len(matched_papers) > 0:
    print('Top 5 papers:')
    for idx, paper in enumerate(matched_papers[:5]):
        title_part = paper['title'][:75]
        year_str = str(paper['year'])
        cite_str = str(paper['total_citations'])
        print(str(idx+1) + '. ' + title_part + ' - Year: ' + year_str + ', Citations: ' + cite_str)

print('__RESULT__:')
print(json.dumps(matched_papers, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': []}

exec(code, env_args)
