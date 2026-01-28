code = """import json
import re

# Load funding data
with open(var_functions.query_db:0, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
with open(var_functions.query_db:2, 'r') as f:
    civic_docs = json.load(f)

print('__RESULT__:')
print(json.dumps({
    "funding_count": len(funding_data),
    "civic_docs_count": len(civic_docs)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
