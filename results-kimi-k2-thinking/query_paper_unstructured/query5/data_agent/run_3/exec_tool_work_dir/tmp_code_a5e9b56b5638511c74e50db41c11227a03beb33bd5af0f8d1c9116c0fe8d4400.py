code = """import json
from collections import defaultdict

citations = locals()['var_functions.query_db:7']
papers = locals()['var_functions.query_db:8']

if isinstance(citations, str):
    with open(citations, 'r') as f:
        citations = json.load(f)

if isinstance(papers, str):
    with open(papers, 'r') as f:
        papers = json.load(f)

print('Total citations:', len(citations))
print('Total papers:', len(papers))

# Examine some samples
print('\nSample citations:')
for i, c in enumerate(citations[:3]):
    print(f"{i+1}. {c}")

print('\nSample papers:')
for i, p in enumerate(papers[:3]):
    print(f"{i+1}. Filename: {p.get('filename')}")
    print(f"   Text: {p.get('text')[:200]}...")

# Look for CHI in papers more carefully
chi_candidates = []
for paper in papers[:50]:  # Check first 50 to see pattern
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '').lower()
    if 'chi' in text or 'chi' in filename:
        chi_candidates.append(paper)

print(f'\nFound {len(chi_candidates)} potential CHI papers in first 50')
for p in chi_candidates[:5]:
    print(f"Filename: {p.get('filename')}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': {'total_chi_citations_2020': 0, 'chi_papers_counted': 0}}

exec(code, env_args)
