code = """import json
# Load the two previous results from storage
# var_call_cRaC5WpgFRCMbonrwxEkmbqO and var_call_Slh1SK1ytJM3LOl8kiDtrKEj

def load_var(v):
    import os
    if isinstance(v, str) and os.path.exists(v):
        with open(v, 'r') as f:
            return json.load(f)
    return v

rl_stockinfo = load_var(var_call_cRaC5WpgFRCMbonrwxEkmbqO)
rl_tables = load_var(var_call_Slh1SK1ytJM3LOl8kiDtrKEj)

# Extract symbols from stockinfo list
symbols_info = {r['Symbol']: r.get('Company Description','') for r in rl_stockinfo}

# Find intersection with available trade tables
available_tables = set(rl_tables)
intersection = [s for s in symbols_info.keys() if s in available_tables]

# Build queries
queries = []
for s in intersection:
    q = f'SELECT "{s}" AS symbol, COUNT(*) AS cnt FROM "{s}" WHERE Date >= \"2019-01-01\" AND Date <= \"2019-12-31\" AND (High - Low) > 0.2 * Low;'
    queries.append({
        'symbol': s,
        'company_description': symbols_info[s],
        'query': q
    })

# Output the list as JSON string
print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_call_cRaC5WpgFRCMbonrwxEkmbqO': 'file_storage/call_cRaC5WpgFRCMbonrwxEkmbqO.json', 'var_call_Slh1SK1ytJM3LOl8kiDtrKEj': 'file_storage/call_Slh1SK1ytJM3LOl8kiDtrKEj.json'}

exec(code, env_args)
