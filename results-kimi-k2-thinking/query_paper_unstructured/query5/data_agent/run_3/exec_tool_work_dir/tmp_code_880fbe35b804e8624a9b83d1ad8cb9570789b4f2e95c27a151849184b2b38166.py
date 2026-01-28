code = """import json, re, os
c_path = locals()['var_functions.query_db:7']
p_path = locals()['var_functions.query_db:8']

with open(c_path) as f:
    citations = json.load(f)
with open(p_path) as f:
    papers = json.load(f)

# Look at a sample of citations from 2020
citations_2020 = [c for c in citations if c.get('citation_year') == 2020]
print('Sample 2020 citation titles (first 10):')
for i, c in enumerate(citations_2020[:10]):
    print(f"  {i+1}. '{c.get('title')}' (count: {c.get('citation_count')})")

# Find CHI papers and show their titles
print('\nCHI papers found (first 10):')
chi_papers = []
for i, paper in enumerate(papers):
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    
    if re.search(r'chi\s+[\'"]?\s*(20)?\d{2}', text, re.IGNORECASE) or 'conference on human factors' in text:
        title = filename.replace('.txt', '')
        chi_papers.append(title)
        if len(chi_papers) <= 10:
            print(f"  {len(chi_papers)}. '{title}'")

print(f'\nTotal CHI papers: {len(chi_papers)}')
print(f'Total 2020 citations: {len(citations_2020)}')

# Check for ANY matches between these sets
citation_titles = [c.get('title', '').lower() for c in citations_2020]
chi_titles = [p.lower() for p in chi_papers]

print('\nDirect exact matches:')
exact_matches = set(citation_titles) & set(chi_titles)
print(f'Found {len(exact_matches)} exact matches')
for match in list(exact_matches)[:5]:
    print(f"  '{match}'")

# Check if we need substring matching
print('\nTrying substring matching...')
substring_matches = []
for ct in citation_titles[:100]:  # Check first 100
    for pt in chi_titles:
        if ct in pt or pt in ct:
            substring_matches.append((ct, pt))
            break

print(f'Found {len(substring_matches)} substring matches in first 100')
for ct, pt in substring_matches[:5]:
    print(f"  Citation: '{ct}'")
    print(f"  Paper:    '{pt}'")

result = {
    'chi_papers_found': len(chi_papers),
    'citations_2020_found': len(citations_2020),
    'exact_matches': len(exact_matches),
    'substring_matches_sample': len(substring_matches)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': {'total_chi_citations_2020': 0, 'chi_papers_counted': 0}, 'var_functions.execute_python:22': {'citations_type': "<class 'str'>", 'papers_type': "<class 'str'>"}, 'var_functions.execute_python:24': {'total_citations': 0, 'papers_matched': 0}, 'var_functions.execute_python:30': {'total_citations_2020': 0, 'chi_papers_counted': 0, 'total_chi_papers': 4}, 'var_functions.execute_python:34': {'total_citations': 0, 'papers_matched': 0, 'chi_papers_found': 0}, 'var_functions.execute_python:36': {'total_citations_2020': 0, 'papers_matched': 0, 'chi_papers_found': 5, 'sample_matches': []}}

exec(code, env_args)
