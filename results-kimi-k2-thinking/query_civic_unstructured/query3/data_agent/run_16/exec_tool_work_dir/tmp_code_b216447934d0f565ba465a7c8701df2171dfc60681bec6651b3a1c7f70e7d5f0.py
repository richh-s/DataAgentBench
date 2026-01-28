code = """import json
import re

# Load funding data from the file
with open('var_functions.query_db:0', 'r') as f:
    funding_data = json.load(f)

# Load civic docs data from the file
with open('var_functions.query_db:2', 'r') as f:
    civic_docs_data = json.load(f)

print(f"__RESULT__:")
print(json.dumps({
    "funding_records_count": len(funding_data),
    "civic_docs_count": len(civic_docs_data),
    "sample_funding": funding_data[:3],
    "sample_civic_doc_keys": list(civic_docs_data[0].keys()) if civic_docs_data else []
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
