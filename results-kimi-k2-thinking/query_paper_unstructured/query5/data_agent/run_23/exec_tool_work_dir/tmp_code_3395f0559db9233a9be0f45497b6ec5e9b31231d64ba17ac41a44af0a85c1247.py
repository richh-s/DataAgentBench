code = """import json
import re
import os

# Debug: list all variables
print('All vars starting with var_:')
for key in list(locals().keys()):
    if key.startswith('var_'):
        print(f'  {key}: {type(locals()[key])}')

# Check if we have the right keys
citations_key = None
paper_key = None
for key in list(locals().keys()):
    if 'query_db:5' in key:
        citations_key = key
    if 'query_db:9' in key:
        paper_key = key

print(f'\nFound keys:')
print(f'  Citations: {citations_key}')
print(f'  Papers: {paper_key}')

# Get the actual data
citations_path = locals()[citations_key] if citations_key else None
paper_path = locals()[paper_key] if paper_key else None

print(f'\nPaths:')
print(f'  Citations path: {citations_path}')
print(f'  Paper path: {paper_path}')

# Load data from files
if citations_path and os.path.exists(citations_path):
    with open(citations_path, 'r') as f:
        citations_2020 = json.load(f)
    print(f'Loaded {len(citations_2020)} citation records')
else:
    citations_2020 = []
    print('No citations data loaded')

if paper_path and os.path.exists(paper_path):
    with open(paper_path, 'r') as f:
        paper_docs = json.load(f)
    print(f'Loaded {len(paper_docs)} paper documents')
else:
    paper_docs = []
    print('No paper docs loaded')

if not citations_2020 or not paper_docs:
    print('ERROR: Missing data')
    exit()

# Process citations
citations_dict = {}
for c in citations_2020:
    citations_dict[c['title']] = int(c['citation_count'])

print(f'Citations dictionary: {len(citations_dict)} entries')

# Find CHI papers - look for CHI conference mentions in text
chi_titles = set()
for doc in paper_docs:
    text = doc['text']
    # Multiple patterns to detect CHI papers
    patterns = [
        r'CHI\s*\'\s*\d{2}',  # CHI '15
        r'CHI\s*\d{4}',      # CHI 2015  
        r'Proceedings of CHI',
        r'ACM.*CHI',
        r'CHI\s+Conference'
    ]
    
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            title = doc['filename'].replace('.txt', '')
            chi_titles.add(title)
            break

print(f'Found {len(chi_titles)} CHI papers')

# Match with 2020 citations
total_citations = 0
matched_papers = []

for title in chi_titles:
    if title in citations_dict:
        count = citations_dict[title]
        total_citations += count
        matched_papers.append({
            'title': title,
            'citations_2020': count
        })

print(f'Matched {len(matched_papers)} CHI papers with 2020 citations')
print(f'Total citations: {total_citations}')

# Sort by citation count
matched_papers.sort(key=lambda x: x['citations_2020'], reverse=True)

print('\nTop CHI papers by 2020 citations:')
for i, paper in enumerate(matched_papers[:10]):
    print(f"  {i+1}. {paper['citations_2020']} - {paper['title'][:60]}...")

result = {'total_citations': total_citations, 'papers_count': len(matched_papers)}
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
