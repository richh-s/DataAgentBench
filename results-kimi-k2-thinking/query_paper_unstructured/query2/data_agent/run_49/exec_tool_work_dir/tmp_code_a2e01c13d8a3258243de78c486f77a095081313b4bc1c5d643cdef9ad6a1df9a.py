code = """import json
import re

citations_file = locals()['var_functions.query_db:0']
if isinstance(citations_file, str):
    with open(citations_file, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_file

papers_file = locals()['var_functions.query_db:5']
if isinstance(papers_file, str):
    with open(papers_file, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = papers_file

print('Total citations in 2018: {}'.format(len(citations_data)))
print('Total paper documents: {}'.format(len(papers_data)))

print('First citation: {}'.format(str(citations_data[0])[:200]))
print('First paper: {}'.format(str(papers_data[0])[:200]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
