code = """import json
import re

# Read the full MongoDB query result
with open('/tmp/tmp8z5d6g7h.json', 'r') as f:
    civic_docs_data = json.load(f)

# Read the full Funding table query result
with open('/tmp/tmpj5w7p9o7.json', 'r') as f:
    funding_data = json.load(f)

print(f"Found {len(civic_docs_data)} documents related to 'emergency' or 'FEMA'")
print(f"Found {len(funding_data)} funding records")

# Let's examine the structure of the data
sample_doc = civic_docs_data[0] if civic_docs_data else None
sample_funding = funding_data[0] if funding_data else None

print("\nSample civic doc keys:", list(sample_doc.keys()) if sample_doc else "No data")
print("Sample funding record:", sample_funding if sample_funding else "No data")

__RESULT__:
print(json.dumps({
    "civic_docs_count": len(civic_docs_data),
    "funding_count": len(funding_data),
    "sample_doc_keys": list(sample_doc.keys()) if sample_doc else None,
    "sample_funding": sample_funding if sample_funding else None
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
