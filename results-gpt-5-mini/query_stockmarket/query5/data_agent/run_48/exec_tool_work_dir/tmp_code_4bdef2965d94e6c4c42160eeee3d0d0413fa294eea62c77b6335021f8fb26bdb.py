code = """import json
with open(var_call_QB0CCR1hatdVEWXkYN8q4fGL, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_5zfSoW9T2RnNqppz3xCdHJon, 'r') as f:
    trade_tables = json.load(f)

s_symbols = []
company_map = {}
for rec in stockinfo:
    sym = rec.get('Symbol')
    desc = rec.get('Company Description')
    if not sym:
        continue
    s_symbols.append(sym)
    company_map[sym] = desc

available_symbols = [s for s in s_symbols if s in trade_tables]

out = {'available_symbols': available_symbols, 'company_map': company_map}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_QB0CCR1hatdVEWXkYN8q4fGL': 'file_storage/call_QB0CCR1hatdVEWXkYN8q4fGL.json', 'var_call_5zfSoW9T2RnNqppz3xCdHJon': 'file_storage/call_5zfSoW9T2RnNqppz3xCdHJon.json'}

exec(code, env_args)
