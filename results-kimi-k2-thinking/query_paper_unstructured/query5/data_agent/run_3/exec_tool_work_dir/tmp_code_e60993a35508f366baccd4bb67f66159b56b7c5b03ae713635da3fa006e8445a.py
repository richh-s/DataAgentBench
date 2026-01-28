code = """import json, re
c_path = locals()['var_functions.query_db:7']
p_path = locals()['var_functions.query_db:8']

with open(c_path) as f:
    citations = json.load(f)
with open(p_path) as f:
    papers = json.load(f)

# Debug: Check data types and values
print('Total citations:', len(citations))
print('Sample citation:', citations[0])
print('Sample citation year type:', type(citations[0].get('citation_year')))
print('Sample citation year value:', repr(citations[0].get('citation_year')))

# Check distinct citation_year values
years = set()
for c in citations:
    year = c.get('citation_year')
    years.add(year)

print('\nDistinct citation_year values (showing first 20):')
for i, year in enumerate(list(years)[:20]):
    print(f'  {i+1}. {repr(year)} (type: {type(year)})')

# Find papers with CHI
chi_papers = []
for p in papers:
    text = p.get('text', '').lower()
    filename = p.get('filename', '').lower()
    if 'chi' in text or 'chi' in filename:
        title = p.get('filename', '').replace('.txt', '')
        chi_papers.append(title.lower())

print(f'\nCHI papers found: {len(chi_papers)}')
for i, title in enumerate(chi_papers[:10]):
    print(f'  {i+1}. {title}')

# Try string comparison for year
c2020 = [c for c in citations if str(c.get('citation_year', '')) == '2020']
print(f'\n2020 citations (string match): {len(c2020)}')

# Try integer comparison
c2020_int = [c for c in citations if c.get('citation_year') == 2020 or c.get('citation_year') == '2020']
print(f'2020 citations (flexible match): {len(c2020_int)}')

result = {
    'total_citations': len(citations),
    'chi_papers': len(chi_papers),
    'c2020_by_string': len(c2020),
    'c2020_flexible': len(c2020_int)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': {'total_chi_citations_2020': 0, 'chi_papers_counted': 0}, 'var_functions.execute_python:22': {'citations_type': "<class 'str'>", 'papers_type': "<class 'str'>"}, 'var_functions.execute_python:24': {'total_citations': 0, 'papers_matched': 0}, 'var_functions.execute_python:30': {'total_citations_2020': 0, 'chi_papers_counted': 0, 'total_chi_papers': 4}, 'var_functions.execute_python:34': {'total_citations': 0, 'papers_matched': 0, 'chi_papers_found': 0}, 'var_functions.execute_python:36': {'total_citations_2020': 0, 'papers_matched': 0, 'chi_papers_found': 5, 'sample_matches': []}, 'var_functions.execute_python:40': {'total': 0, 'papers': 0, 'chi_total': 5, 'c2020_total': 0}}

exec(code, env_args)
