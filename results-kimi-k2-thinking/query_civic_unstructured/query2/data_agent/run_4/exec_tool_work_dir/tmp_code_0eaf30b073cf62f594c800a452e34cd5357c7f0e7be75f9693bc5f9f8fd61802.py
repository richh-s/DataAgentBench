code = """import json

# Load the data from the files
civic_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:6']

with open(civic_path, 'r') as f:
    civic_data = json.load(f)
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Debug: see first part of first civic doc
first_doc_text = civic_data[0]['text'][:1000] if civic_data else "No data"

print('__RESULT__:')
print(json.dumps({
    'civic_docs_count': len(civic_data),
    'funding_records_count': len(funding_records),
    'sample_text': first_doc_text
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.list_db:4', 'var_functions.query_db:6', '__builtins__', 'json'], 'var_functions.execute_python:14': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_sample_keys': ['_id', 'filename', 'text'], 'funding_sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.execute_python:36': {'civic_type': "<class 'str'>", 'funding_type': "<class 'str'>", 'civic_is_file': True, 'funding_is_file': True}}

exec(code, env_args)
