code = """import json
import re

# Load full results from previous queries
# funding_results = var_functions.query_db:5  # This is the path to the file
# civic_results = var_functions.query_db:6    # This is the path to the file

# Since the results are paths to JSON files, I need to read them
with open(var_functions.query_db:5, 'r') as f:
    funding_data = json.load(f)

with open(var_functions.query_db:6, 'r') as f:
    civic_data = json.load(f)

# Let's see what we have
print('__RESULT__:')
print(json.dumps({
    "funding_records_count": len(funding_data),
    "civic_documents_count": len(civic_data),
    "sample_funding": funding_data[:3],
    "sample_civic": civic_data[:2]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
