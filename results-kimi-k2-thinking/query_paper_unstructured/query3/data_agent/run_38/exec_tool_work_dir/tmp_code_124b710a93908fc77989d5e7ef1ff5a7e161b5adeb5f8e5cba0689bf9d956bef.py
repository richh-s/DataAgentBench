code = """import json
import re

# Debug: check what type of data we have
papers_var = locals()['var_functions.query_db:30']
citations_var = locals()['var_functions.query_db:28']

print('papers_var type:', type(papers_var))
print('citations_var type:', type(citations_var))

# If they're strings (file paths), we need to load them
if isinstance(papers_var, str):
    with open(papers_var, 'r') as f:
        papers_data = json.load(f)
else:
    papers_data = papers_var

if isinstance(citations_var, str):
    with open(citations_var, 'r') as f:
        citations_data = json.load(f)
else:
    citations_data = citations_var

print('papers_data type:', type(papers_data))
print('citations_data type:', type(citations_data))
print('papers_data length:', len(papers_data))
print('citations_data length:', len(citations_data))

# Show first item of each to verify structure
print('First paper item:', papers_data[0] if papers_data else 'Empty')
print('First citation item:', citations_data[0] if citations_data else 'Empty')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
