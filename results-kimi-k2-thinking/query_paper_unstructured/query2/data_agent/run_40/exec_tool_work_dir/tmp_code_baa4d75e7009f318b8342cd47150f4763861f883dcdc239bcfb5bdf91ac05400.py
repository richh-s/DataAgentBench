code = """import json
import re

# Read the citation data for 2018
citations_file = var_functions.query_db_0
if isinstance(citations_file, str) and citations_file.endswith('.json'):
    with open(citations_file, 'r') as f:
        citations_2018 = json.load(f)
else:
    citations_2018 = var_functions.query_db_0

# Read the paper documents
papers_file = var_functions.query_db_2
if isinstance(papers_file, str) and papers_file.endswith('.json'):
    with open(papers_file, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = var_functions.query_db_2

print('Loaded data successfully')
print(f'Citations 2018 count: {len(citations_2018)}')
print(f'Paper docs count: {len(paper_docs)}')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
