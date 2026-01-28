code = """import json
import re

# Get civic documents data
civic_docs_input = locals().get('var_functions.query_db:5', [])
civic_docs = civic_docs_input
if isinstance(civic_docs_input, str):
    try:
        with open(civic_docs_input, 'r') as f:
            civic_docs = json.load(f)
    except:
        civic_docs = []

# Get funding data
funding_input = locals().get('var_functions.query_db:8', [])
funding_data = funding_input
if isinstance(funding_input, str):
    try:
        with open(funding_input, 'r') as f:
            funding_data = json.load(f)
    except:
        funding_data = []

# Output the count info
output = {
    "total_civic_docs": len(civic_docs),
    "total_funding_records": len(funding_data)
}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
