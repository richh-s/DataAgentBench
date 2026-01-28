code = """import json
import re

# Check what type of data we have
citations_result = var_functions.query_db:5
paper_docs_result = var_functions.query_db:9

print("Type of citations_result:", type(citations_result))
print("Type of paper_docs_result:", type(paper_docs_result))

# If they are strings (file paths), load them
if isinstance(citations_result, str):
    with open(citations_result, 'r') as f:
        citations_2020 = json.load(f)
else:
    citations_2020 = citations_result

if isinstance(paper_docs_result, str):
    with open(paper_docs_result, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_result

print(f"Total 2020 citations records: {len(citations_2020)}")
print(f"Total paper documents: {len(paper_docs)}")

# Create mapping of paper titles to documents
paper_dict = {}
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    paper_dict[title] = doc

print(f"Number of papers mapped: {len(paper_dict)}")

__RESULT__: 
print("Data loaded successfully")"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
