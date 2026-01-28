code = """import json
import re

# Load the full paper documents data
paper_docs_path = locals()['var_functions.query_db:12']
paper_citations_path = locals()['var_functions.query_db:12']

# Read paper documents
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Read citation data
with open(paper_citations_path, 'r') as f:
    citations = json.load(f)

print("Paper documents:", len(paper_docs))
print("Citations records:", len(citations))
print("First paper filename:", paper_docs[0]['filename'])
print("First citation title:", citations[0]['title'])"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
