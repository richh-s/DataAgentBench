code = """import json
import re

# Load citations data
citations_path = locals()['var_functions.query_db:38']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Load paper documents
papers_path = locals()['var_functions.query_db:28']
with open(papers_path, 'r') as f:
    papers = json.load(f)

print('Loaded', len(citations), 'citations and', len(papers), 'papers')

# Find empirical papers after 2016
empirical_titles = []
for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    
    if not text or not filename:
        continue
    
    # Extract year from beginning of text
    year_match = re.search(r'(\b20\d{2}\b)', text[:2000])
    year = int(year_match.group(1)) if year_match else None
    
    # Check if paper mentions empirical
    is_empirical = 'empirical' in text.lower()
    
    if year and year > 2016 and is_empirical:
        title = filename.replace('.txt', '')
        empirical_titles.append(title)

print('Found', len(empirical_titles), 'empirical papers after 2016')

# Build citation lookup
citation_lookup = {}
for c in citations:
    citation_lookup[c['title']] = int(c['total_citations'])

# Get results with citations
results = []
for title in empirical_titles:
    if title in citation_lookup:
        results.append({'title': title, 'total_citations': citation_lookup[title]})

# Sort by citation count
results.sort(key=lambda x: x['total_citations'], reverse=True)

print('Final results:', len(results))

# Output in required format
output = json.dumps(results)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:32': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
