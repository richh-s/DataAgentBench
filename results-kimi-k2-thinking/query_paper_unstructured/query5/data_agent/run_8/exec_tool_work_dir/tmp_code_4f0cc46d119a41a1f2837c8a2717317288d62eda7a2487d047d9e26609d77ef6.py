code = """import json
import re

# Get stored file paths
citations_file = locals()['var_functions.query_db:26']
papers_file = locals()['var_functions.query_db:10']

print(f'Citations file: {citations_file}')
print(f'Papers file: {papers_file}')

# Load data
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

with open(papers_file, 'r') as f:
    papers = json.load(f)

print(f'Loaded {len(citations_2020)} citations for 2020')
print(f'Loaded {len(papers)} papers')

# Identify CHI papers
chi_titles = []
for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check for CHI conference mentions
    if re.search(r'CHI\s*\'\d{2}', text, re.I) or re.search(r'CHI\s*20\d{2}', text, re.I):
        chi_titles.append(title)

print(f'Found {len(chi_titles)} CHI papers')

# Sum citations for CHI papers
total_citations = 0
for citation in citations_2020:
    if citation['title'] in chi_titles:
        total_citations += int(citation['citation_count'])

result = {'total_citations_2020': total_citations}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
