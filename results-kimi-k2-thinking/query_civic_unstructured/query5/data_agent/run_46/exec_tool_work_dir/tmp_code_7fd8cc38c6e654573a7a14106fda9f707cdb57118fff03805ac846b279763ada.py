code = """import json
import re

# Access the data from storage
civic_docs = locals()['var_functions.query_db:5']
funding_data = locals()['var_functions.query_db:2']

print(f"__RESULT__: ")
print(json.dumps({
    "civic_docs_count": len(civic_docs),
    "funding_count": len(funding_data),
    "sample_doc_keys": list(civic_docs[0].keys()) if civic_docs else [],
    "sample_funding_keys": list(funding_data[0].keys()) if funding_data else []
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
