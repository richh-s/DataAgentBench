code = """import json, re
c_path = locals()['var_functions.query_db:7']
p_path = locals()['var_functions.query_db:8']

with open(c_path) as f:
    citations = json.load(f)
with open(p_path) as f:
    papers = json.load(f)

# Debug the data
print('Total citations:', len(citations))
print('First citation:', citations[0])

# Find distinct years
years = {}
for c in citations:
    year = c.get('citation_year')
    years[year] = years.get(year, 0) + 1

print('\nYear distribution (showing first 20):')
for year in list(years.keys())[:20]:
    print(' ', repr(year), ':', years[year])

# Find CHI papers
chi_papers = []
for p in papers[:200]:  # Check first 200 to see pattern
    text = p.get('text', '').lower()
    filename = p.get('filename', '').lower()
    if 'chi' in text or 'chi' in filename:
        title = p.get('filename', '').replace('.txt', '')
        chi_papers.append(title.lower())

print('\nCHI papers found (first 200 papers):', len(chi_papers))
for title in chi_papers[:10]:
    print(' ', title)

# Try to find 2020 citations
c2020 = []
for c in citations:
    year = c.get('citation_year')
    if str(year) == '2020' or year == 2020:
        c2020.append(c)

print('\n2020 citations found:', len(c2020))
for c in c2020[:5]:
    print(' ', c.get('title'))

result = {
    'total_citations': len(citations),
    'chi_papers': len(chi_papers),
    'c2020_citations': len(c2020)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': {'total_chi_citations_2020': 0, 'chi_papers_counted': 0}, 'var_functions.execute_python:22': {'citations_type': "<class 'str'>", 'papers_type': "<class 'str'>"}, 'var_functions.execute_python:24': {'total_citations': 0, 'papers_matched': 0}, 'var_functions.execute_python:30': {'total_citations_2020': 0, 'chi_papers_counted': 0, 'total_chi_papers': 4}, 'var_functions.execute_python:34': {'total_citations': 0, 'papers_matched': 0, 'chi_papers_found': 0}, 'var_functions.execute_python:36': {'total_citations_2020': 0, 'papers_matched': 0, 'chi_papers_found': 5, 'sample_matches': []}, 'var_functions.execute_python:40': {'total': 0, 'papers': 0, 'chi_total': 5, 'c2020_total': 0}}

exec(code, env_args)
