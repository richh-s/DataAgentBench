code = """import json
import re

# Read civic documents from file
civic_file_path = locals()['var_functions.query_db:8']
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Read funding data from file
funding_file_path = locals()['var_functions.query_db:2']
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Debug: print counts
print('__RESULT__:')
print(json.dumps({
    'civic_docs_count': len(civic_docs),
    'funding_records_count': len(funding_data),
    'funding_sample': funding_data[:2]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'record_count': 276, 'sample_project_names': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
