code = """import json

# Load funding data
funding_path = locals()['var_functions.query_db:0']
if isinstance(funding_path, str):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = locals()['var_functions.query_db:0']

# Load civic docs data  
civic_docs_path = locals()['var_functions.query_db:2']
if isinstance(civic_docs_path, str):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = locals()['var_functions.query_db:2']

# Identify disaster-related projects and get their funding
print('__RESULT__')
print(json.dumps({
    'funding_count': len(funding_data),
    'civic_doc_count': len(civic_docs),
    'first_funding_sample': funding_data[0] if funding_data else None
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': 'file_storage/functions.execute_python:4.json', 'var_functions.execute_python:12': {'funding_records': 500, 'civic_docs': 5}, 'var_functions.execute_python:14': {'civic_docs_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'civic_docs_full_count': 5, 'sample_doc_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:20': {'civic_docs_total': 5, 'funding_records_total': 500, 'sample_doc_filename': 'malibucity_agenda_03222023-2060.txt'}}

exec(code, env_args)
