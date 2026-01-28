code = """import json
import re

# Load funding data
funding_file = var_functions.query_db:4
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = var_functions.query_db:5
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print("__RESULT__:")
print(json.dumps({
    "funding_records": len(funding_data),
    "civic_docs": len(civic_docs),
    "sample_funding": funding_data[:2] if funding_data else [],
    "sample_civic": civic_docs[0]['text'][:500] if civic_docs else ""
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': ['var_functions.list_db:0', 'var_functions.list_db:1', 'var_functions.query_db:4', 'var_functions.query_db:5']}

exec(code, env_args)
