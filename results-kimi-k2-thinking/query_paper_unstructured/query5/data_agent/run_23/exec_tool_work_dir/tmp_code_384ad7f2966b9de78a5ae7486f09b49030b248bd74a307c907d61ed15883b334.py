code = """import json
import re

# List all variables available
all_vars = list(locals().keys())
print('Available variables:')
print([v for v in all_vars if v.startswith('var_')])

# Let's access the results by their keys
citations_key = 'var_functions.query_db:5'
paper_key = 'var_functions.query_db:9'

if citations_key in locals():
    citations_2020 = locals()[citations_key]
    print('Cit found, type:', type(citations_2020))
    print('Cit length:', len(citations_2020))
else:
    print('Citations key not found')

if paper_key in locals():
    paper_docs = locals()[paper_key]
    print('Paper found, type:', type(paper_docs))
    print('Paper length:', len(paper_docs))
else:
    print('Paper key not found')

# Create citations dictionary
citations_dict = {}
for c in citations_2020:
    citations_dict[c['title']] = int(c['citation_count'])

print('Citations dict size:', len(citations_dict))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
