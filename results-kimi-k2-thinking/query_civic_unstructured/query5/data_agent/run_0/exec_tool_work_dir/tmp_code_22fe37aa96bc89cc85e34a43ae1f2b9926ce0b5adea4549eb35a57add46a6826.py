code = """import json
import re
from pathlib import Path

# Read funding data from file
funding_file = var_functions.query_db:2
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Read civic docs data from file
civic_file = var_functions.query_db:3
with open(civic_file, 'r') as f:
    civic_docs_data = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'funding_count': len(funding_data),
    'civic_docs_count': len(civic_docs_data),
    'sample_funding': funding_data[:2],
    'sample_civic': str(civic_docs_data[0])[:200]
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
