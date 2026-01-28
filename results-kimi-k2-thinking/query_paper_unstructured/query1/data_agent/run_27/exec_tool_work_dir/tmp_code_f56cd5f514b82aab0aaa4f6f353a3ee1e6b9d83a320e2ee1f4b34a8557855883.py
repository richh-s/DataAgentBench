code = """import json
import os

# Check what types our variables are
paper_docs_var = locals()['var_functions.query_db:8']
citations_var = locals()['var_functions.query_db:12']

print(f"Types: paper_docs_var={type(paper_docs_var)}, citations_var={type(citations_var)}")

# Handle paper_docs
if isinstance(paper_docs_var, list):
    paper_docs = paper_docs_var
else:
    # It's likely a file path
    with open(paper_docs_var, 'r') as f:
        paper_docs = json.load(f)

# Handle citations  
if isinstance(citations_var, list):
    citations = citations_var
else:
    # It's likely a file path
    with open(citations_var, 'r') as f:
        citations = json.load(f)

print(f"Data loaded: {len(paper_docs)} papers, {len(citations)} citations")

# Identify food papers
food_paper_titles = []
for paper in paper_docs:
    title = paper['filename'].replace('.txt', '')
    if 'food' in paper.get('text', '').lower():
        food_paper_titles.append(title)

print(f"Found {len(food_paper_titles)} food-related papers")

# Calculate total citations
total_citations = sum(int(c['citation_count']) for c in citations if c['title'] in food_paper_titles)
print(f"Total citations for food papers: {total_citations}")

print('__RESULT__:')
print(json.dumps(total_citations))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
