code = """import json
import re

# Debug: check the type of citations data
citations_debug = locals()['var_functions.query_db:16']
print('Type of citations_data:', type(citations_debug))
print('First 200 chars:', str(citations_debug)[:200])

# If it's a string (file path), load it
if isinstance(citations_debug, str) and 'json' in citations_debug:
    with open(citations_debug, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_debug

# Load the paper documents data from the file
papers_file_path = locals()['var_functions.query_db:17']
with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

# Convert citation_count to integers properly
for citation in citations_data:
    if 'citation_count' in citation:
        citation['citation_count'] = int(str(citation['citation_count']))

print('Total citations records:', len(citations_data))
print('Sample citation:', citations_data[0])
print('Total papers documents:', len(papers_data))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
