code = """import json
import re

# Load the full civic docs data from the file
with open('civic_docs_data.json', 'r') as f:
    civic_docs = json.load(f)

# Load the funding data from the file  
with open('funding_data.json', 'r') as f:
    funding_data = json.load(f)

print("__RESULT__:")
result = {
    "civic_docs_count": len(civic_docs),
    "funding_records_count": len(funding_data),
    "first_doc_keys": list(civic_docs[0].keys()),
    "sample_text": civic_docs[0]['text'][:500]
}
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
