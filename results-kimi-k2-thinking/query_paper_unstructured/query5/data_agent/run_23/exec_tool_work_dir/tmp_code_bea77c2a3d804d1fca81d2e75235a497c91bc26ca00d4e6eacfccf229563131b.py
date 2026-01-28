code = """import json
import re

# Access stored results - they are available as variables
citations_data = var_functions.query_db_5
paper_data = var_functions.query_db_9

# Debug: print types
print("Types:", type(citations_data), type(paper_data))
print("First citation:", citations_data[0] if citations_data else "No data")
print("First paper:", paper_data[0]['filename'] if paper_data else "No data")

# Create citations dictionary
citations_dict = {}
for c in citations_data:
    citations_dict[c['title']] = int(c['citation_count'])

# Find CHI papers
chi_titles = []
for doc in paper_data:
    text = doc['text']
    if 'CHI' in text:
        title = doc['filename'].replace('.txt', '')
        chi_titles.append(title)

print(f"Found {len(chi_titles)} potential CHI papers")

# Match and sum citations
total = 0
count = 0
for title in chi_titles:
    if title in citations_dict:
        total += citations_dict[title]
        count += 1

print(f"{count} CHI papers had 2020 citations, total: {total}")

__RESULT__ = total
print("__RESULT__:")
print(json.dumps(__RESULT__))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
