code = """import json
import re

# Read the civic documents data
civic_docs_path = locals()['var_functions.query_db:5']
if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = locals()['var_functions.query_db:5']

# Read the funding data
funding_path = locals()['var_functions.query_db:8']
if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = locals()['var_functions.query_db:8']

# Show summary of data
print("__RESULT__:")
print(json.dumps({
    "civic_docs_count": len(civic_docs),
    "funding_records_count": len(funding_data),
    "sample_civic_doc_keys": list(civic_docs[0].keys()) if civic_docs else [],
    "sample_funding_keys": list(funding_data[0].keys()) if funding_data else [],
    "sample_civic_text_preview": civic_docs[0]['text'][:500] if civic_docs else ""
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
