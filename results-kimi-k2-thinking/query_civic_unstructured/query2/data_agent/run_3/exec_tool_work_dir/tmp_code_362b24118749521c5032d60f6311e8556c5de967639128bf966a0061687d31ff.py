code = """import json
from pathlib import Path

# Read funding data
funding_path = locals()['var_functions.query_db:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Read civic documents data
civic_path = locals()['var_functions.query_db:3']
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'funding_count': len(funding_data),
    'civic_count': len(civic_data),
    'funding_sample': funding_data[:3],
    'civic_sample': [{'filename': doc.get('filename'), 'text_preview': doc.get('text', '')[:200]} for doc in civic_data[:2]]
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
