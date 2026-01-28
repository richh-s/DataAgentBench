code = """import json
import pandas as pd

# The results are stored in variables automatically
# Let's check what we have access to

# Directly access the large result files
# Read the citations data for 2020
citations_2020_file = "tmptmp1e1p6f.json"
citations_all_file = "tmptmp3q8m8q2r.json"
papers_file = "tmptmpf_9r5s6n.json"

# Try to read these files
import os
print('Checking /tmp directory...')
for f in os.listdir('/tmp'):
    print(f)
    if f.startswith('tmp'):
        print(f'  Found file: {f}')

# Read the actual data files
with open('/tmp/tmptmpn2tux2v2.json', 'r') as f:
    citations_2020 = json.load(f)

with open('/tmp/tmptmpf_9r5s6n.json', 'r') as f:
    paper_docs = json.load(f)

print('Successfully loaded:')
print(f'  - 2020 citations: {len(citations_2020)} records')
print(f'  - Paper documents: {len(paper_docs)} records')

# Now identify CHI papers
chi_paper_titles = []
for i, paper in enumerate(paper_docs):
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    full_text = paper.get('text', '')
    
    # Detect CHI venue by looking for conference indicators
    patterns = ['CHI', 'CHI \'', 'Proceedings of CHI']
    for pattern in patterns:
        if pattern in full_text:
            chi_paper_titles.append(title)
            break

print(f'Identified {len(chi_paper_titles)} papers from CHI venue')

# Create citation lookup for 2020
citation_2020_dict = {c['title']: int(c['citation_count']) for c in citations_2020}

# Match and sum citations
total_citations = 0
matched_papers = 0

for title in chi_paper_titles:
    if title in citation_2020_dict:
        total_citations += citation_2020_dict[title]
        matched_papers += 1

print(f'Matched {matched_papers} CHI papers with 2020 citation data')
print(f'Total citations in 2020 for CHI papers: {total_citations}')

result = {
    'total_citation_count_2020': total_citations,
    'chi_papers_count': len(chi_paper_titles),
    'matched_papers': matched_papers
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:30': {'files': []}, 'var_functions.execute_python:32': {'files': []}}

exec(code, env_args)
