code = """import json
import re

# Read the full paper documents data
file_path = locals()['var_functions.query_db:5']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

# Examine a few papers to understand structure
sample_papers = []
for i, doc in enumerate(paper_docs[:10]):
    title = doc.get('filename', '').replace('.txt', '')
    text = doc.get('text', '')[:1000]  # First 1000 chars
    sample_papers.append({
        'index': i,
        'title': title,
        'preview': text[:500]
    })

print('__RESULT__:')
print(json.dumps(sample_papers, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'empirical_papers_count': 0, 'sample_papers': []}}

exec(code, env_args)
