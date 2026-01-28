code = """import json
import re

# Load the funding data
funding_path = locals()['var_functions.query_db:0']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load the civic docs data
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print("__RESULT__:")
print(json.dumps({
    "funding_records_count": len(funding_data),
    "civic_docs_count": len(civic_docs),
    "sample_funding": funding_data[:3],
    "sample_civic_doc": civic_docs[0] if civic_docs else None
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
