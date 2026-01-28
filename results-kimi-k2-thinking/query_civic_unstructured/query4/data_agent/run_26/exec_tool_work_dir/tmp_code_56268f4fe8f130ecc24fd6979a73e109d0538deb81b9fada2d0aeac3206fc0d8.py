code = """# Load and examine the data
import json

# Load the civic documents data
civic_docs_file = "var_functions.query_db:0"
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load the funding data
funding_file = "var_functions.query_db:5"
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print("__RESULT__:")
print(json.dumps({
    "civic_docs_count": len(civic_docs),
    "funding_records_count": len(funding_data),
    "civic_doc_sample": civic_docs[0] if civic_docs else None,
    "funding_sample": funding_data[0] if funding_data else None
}, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
