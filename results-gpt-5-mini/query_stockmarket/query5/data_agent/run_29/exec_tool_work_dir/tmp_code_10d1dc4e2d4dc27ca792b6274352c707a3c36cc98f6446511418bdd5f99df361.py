code = """import json
# Load the previous query_db and list_db results from files
p1 = var_call_lVKxD92HzNaiKUXndMltg3KE
p2 = var_call_6DFfRUD8huR0gJBPwXJDs37m

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

stockinfo_records = load_json(p1)
stocktrade_tables = load_json(p2)

stockinfo_symbols = [r['Symbol'] for r in stockinfo_records]

# Compute intersection
set_trade = set(stocktrade_tables)
intersect = sorted([s for s in stockinfo_symbols if s in set_trade])

import json
print("__RESULT__:")
print(json.dumps(intersect))"""

env_args = {'var_call_lVKxD92HzNaiKUXndMltg3KE': 'file_storage/call_lVKxD92HzNaiKUXndMltg3KE.json', 'var_call_6DFfRUD8huR0gJBPwXJDs37m': 'file_storage/call_6DFfRUD8huR0gJBPwXJDs37m.json'}

exec(code, env_args)
