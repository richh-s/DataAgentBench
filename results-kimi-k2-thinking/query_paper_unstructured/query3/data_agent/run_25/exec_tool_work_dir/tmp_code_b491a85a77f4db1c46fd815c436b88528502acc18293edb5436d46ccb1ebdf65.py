code = """import json
import re

# Load data
citation_path = locals()['var_functions.query_db:0']
mongodb_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(mongodb_path, 'r') as f:
    papers = json.load(f)

# Debug: Check year distribution and empirical papers
year_counts = {}
emp_counts = {}
emp_after_2016_titles = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    years = re.findall(r'\b(20[0-2][0-9])\b', text)
    year = int(years[0]) if years else 0
    
    has_empirical = 'empirical' in text.lower()
    
    if year:
        year_counts[year] = year_counts.get(year, 0) + 1
        if has_empirical:
            emp_counts[year] = emp_counts.get(year, 0) + 1
            if year > 2016:
                emp_after_2016_titles.append(title)

# Show year distributions
print('Year distribution in papers:')
for year in sorted(year_counts.keys()):
    print(str(year) + ': ' + str(year_counts[year]) + ' total, ' + str(emp_counts.get(year, 0)) + ' empirical')

print('\nEmpirical papers after 2016: ' + str(len(emp_after_2016_titles)))

# Check citation titles
citation_titles = set(c['title'] for c in citations)
print('Total citation titles: ' + str(len(citation_titles)))

# Find matches using normalized titles
norm_citation_map = {}
for c in citations:
    norm_title = re.sub(r'[^a-zA-Z0-9]', '', c['title'].lower())
    norm_citation_map[norm_title] = int(c['total_citations'])

# Find matching empirical papers
final_results = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    years = re.findall(r'\b(20[0-2][0-9])\b', text)
    year = int(years[0]) if years else 0
    
    has_empirical = 'empirical' in text.lower()
    
    if year > 2016 and has_empirical:
        norm_title = re.sub(r'[^a-zA-Z0-9]', '', title.lower())
        if norm_title in norm_citation_map:
            final_results.append({
                'title': title,
                'year': year,
                'total_citations': norm_citation_map[norm_title]
            })

# Sort and output
final_results.sort(key=lambda x: x['total_citations'], reverse=True)

print('\nFinal matched results: ' + str(len(final_results)))
for i, paper in enumerate(final_results[:10]):
    print(str(i+1) + '. ' + paper['title'][:80] + '...')
    print('   Year: ' + str(paper['year']) + ', Citations: ' + str(paper['total_citations']))

print('__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': []}

exec(code, env_args)
