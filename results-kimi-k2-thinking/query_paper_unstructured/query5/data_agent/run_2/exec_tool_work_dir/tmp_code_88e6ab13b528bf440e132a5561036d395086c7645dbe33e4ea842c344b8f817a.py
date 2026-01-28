code = """import json
import os

# Access the stored query results
citations_2020_key = 'var_functions.query_db:20'
paper_docs_key = 'var_functions.query_db:22'

# Get the stored values
citations_2020_path = locals()[citations_2020_key]
paper_docs_path = locals()[paper_docs_key]

print('2020 citations file:', citations_2020_path)
print('Paper docs file:', paper_docs_path)

# Load the data
with open(citations_2020_path, 'r') as f:
    citations_2020 = json.load(f)

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

print(f'Loaded {len(citations_2020)} citations from 2020')
print(f'Loaded {len(paper_docs)} paper documents')

# Identify CHI papers
chi_paper_titles = []
for paper in paper_docs:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    full_text = paper.get('text', '')
    
    # Detect CHI conference papers
    if 'CHI' in full_text:
        chi_paper_titles.append(title)

print(f'Identified {len(chi_paper_titles)} papers from CHI venue')

# Calculate total citations for CHI papers in 2020
# Create a dictionary for quick lookup
citation_lookup = {c['title']: int(c['citation_count']) for c in citations_2020}

total_citations_2020 = 0
matched_papers = 0

for title in chi_paper_titles:
    if title in citation_lookup:
        total_citations_2020 += citation_lookup[title]
        matched_papers += 1

print(f'Matched {matched_papers} CHI papers with 2020 citation data')
print(f'Total citations: {total_citations_2020}')

# Prepare result
result = {
    'total_citation_count': total_citations_2020
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:30': {'files': []}, 'var_functions.execute_python:32': {'files': []}}

exec(code, env_args)
