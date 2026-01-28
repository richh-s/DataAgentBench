code = """import json
import re

# Read the full paper documents data
file_path = 'file_storage/functions.query_db:18.json'
with open(file_path, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(paper_docs),
    'sample_paper': paper_docs[0]['filename'] if paper_docs else None
}))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'total_records': 158, 'sample_records': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58'}]}, 'var_functions.list_db:16': ['paper_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
