code = """import json

# Load data files
civic_docs_file = locals()['var_functions.query_db:5']
funding_file = locals()['var_functions.query_db:6']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(json.dumps({
    'civic_docs_count': len(civic_docs),
    'funding_count': len(funding_data),
    'first_doc_keys': list(civic_docs[0].keys()) if civic_docs else [],
    'first_funding_keys': list(funding_data[0].keys()) if funding_data else [],
    'sample_civic_text': civic_docs[0]['text'][:500] if civic_docs else 'No data',
    'sample_funding': funding_data[0] if funding_data else 'No data'
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 5, 'funding_records_count': 500, 'civic_docs_sample': "{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt', 'text': 'Public Works Commission\\nAgenda Report\\n\\nPublic Works\\nCommission Meeting\\n03-22-23\\nItem\\n4.B.\\n\\nTo:\\"}}

exec(code, env_args)
