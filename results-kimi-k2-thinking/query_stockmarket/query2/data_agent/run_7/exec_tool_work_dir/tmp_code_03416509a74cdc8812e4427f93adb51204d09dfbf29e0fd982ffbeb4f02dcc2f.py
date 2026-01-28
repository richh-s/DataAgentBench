code = """import json
import os

db_result_path = locals().get('var_functions.query_db:0')
if db_result_path and os.path.exists(db_result_path):
    with open(db_result_path, 'r') as f:
        etf_symbols = json.load(f)
else:
    # Fallback if direct variable access works
    etf_symbols = locals().get('var_functions.query_db:0', [])

print('__RESULT__:')
print(json.dumps({'count': len(etf_symbols), 'sample': etf_symbols[:10]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
