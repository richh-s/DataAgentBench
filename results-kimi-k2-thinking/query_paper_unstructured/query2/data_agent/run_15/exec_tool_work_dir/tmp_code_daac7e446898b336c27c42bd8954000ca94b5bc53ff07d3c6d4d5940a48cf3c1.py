code = """import json
import re

# Load the full citations data for 2018
citations_file_path = locals()['var_functions.query_db:9']
with open(citations_file_path, 'r') as f:
    citations_2018 = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'citation_titles_2018': [c['title'] for c in citations_2018[:10]],
    'total_citations_2018': len(citations_2018)
}))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'citations_2018_count': 158, 'paper_docs_count': 5}, 'var_functions.execute_python:14': {'total_citations_2018': 158, 'matched_papers': 0, 'unmatched_papers': 156, 'acm_papers_2018': 0, 'acm_papers_sample': []}}

exec(code, env_args)
