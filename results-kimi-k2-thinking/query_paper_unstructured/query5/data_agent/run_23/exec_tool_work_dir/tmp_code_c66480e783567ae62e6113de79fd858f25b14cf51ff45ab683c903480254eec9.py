code = """import json
import re
import os

# Debug available variables
citations_2020 = None
paper_docs = None

for key in list(locals().keys()):
    if 'query_db' in key and ':5' in key:
        citations_path = locals()[key]
        if isinstance(citations_path, str) and os.path.exists(citations_path):
            with open(citations_path, 'r') as f:
                citations_2020 = json.load(f)
    elif 'query_db' in key and ':9' in key:
        paper_path = locals()[key]
        if isinstance(paper_path, str) and os.path.exists(paper_path):
            with open(paper_path, 'r') as f:
                paper_docs = json.load(f)

if not citations_2020 or not paper_docs:
    print('Could not load data')
    exit()

print('Loaded', len(citations_2020), 'citation records and', len(paper_docs), 'papers')

# Build citations lookup
citations_lookup = {}
for rec in citations_2020:
    citations_lookup[rec['title']] = int(rec['citation_count'])

# Find CHI papers
chi_titles = set()
for doc in paper_docs:
    text = doc['text']
    if 'CHI' in text:
        title = doc['filename'].replace('.txt', '')
        chi_titles.add(title)

print('Found', len(chi_titles), 'CHI papers')

# Calculate total citations
total = 0
matches = 0
for title in chi_titles:
    if title in citations_lookup:
        total += citations_lookup[title]
        matches += 1

print('Matches:', matches, 'Total citations:', total)

result = {'total_citations': total, 'papers_matched': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
