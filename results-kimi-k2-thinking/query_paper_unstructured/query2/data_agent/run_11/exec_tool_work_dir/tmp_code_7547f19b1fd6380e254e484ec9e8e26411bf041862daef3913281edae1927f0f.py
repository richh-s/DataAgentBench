code = """import json

# Debug - get the variable names
vars_dict = {}
for k, v in locals().items():
    if 'query_db' in k:
        vars_dict[k] = v

print('Available variables:', list(vars_dict.keys()))

# Load the 2018 citations
citations_path = vars_dict['var_functions.query_db:70']
with open(citations_path, 'r') as f:
    citations_2018 = json.load(f)

# Load the paper documents  
papers_path = vars_dict['var_functions.query_db:64']
with open(papers_path, 'r') as f:
    paper_docs = json.load(f)

print('Loaded %d citations and %d papers' % (len(citations_2018), len(paper_docs)))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:20': ['paper_docs'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:32': [{'total_2018': '158'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:52': {'total_2018': 158, 'acm_papers': 2, 'avg_citations': 68.5, 'sample_counts': [50, 87]}, 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.query_db:60': [], 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json'}

exec(code, env_args)
