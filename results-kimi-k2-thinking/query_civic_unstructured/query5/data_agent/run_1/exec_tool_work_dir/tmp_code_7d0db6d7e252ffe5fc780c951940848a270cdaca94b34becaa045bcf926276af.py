code = """import json

# Access civic documents data
civic_docs_result = locals()['var_functions.query_db:0']
civic_docs = []
if isinstance(civic_docs_result, str) and civic_docs_result.endswith('.json'):
    with open(civic_docs_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = list(civic_docs_result) if civic_docs_result else []

# Access funding data
funding_result = locals()['var_functions.query_db:7']
funding_data = []
if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = list(funding_result) if funding_result else []

result_info = {
    'civic_docs_count': len(civic_docs),
    'funding_records_count': len(funding_data),
    'first_civic_doc_sample': civic_docs[0]['text'][:200] if civic_docs else None,
    'first_funding_sample': funding_data[0] if funding_data else None,
    'disaster_funding_count': 0,
    'sample_disaster_names': []
}

# Count disaster-related funding records
for record in funding_data:
    name = record.get('Project_Name', '')
    if any(marker in name for marker in ['(FEMA', '(CalOES', '(CalJPIA']):
        result_info['disaster_funding_count'] += 1
        if len(result_info['sample_disaster_names']) < 5:
            result_info['sample_disaster_names'].append(name)

print('__RESULT__:')
print(json.dumps(result_info))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.list_db:3': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
