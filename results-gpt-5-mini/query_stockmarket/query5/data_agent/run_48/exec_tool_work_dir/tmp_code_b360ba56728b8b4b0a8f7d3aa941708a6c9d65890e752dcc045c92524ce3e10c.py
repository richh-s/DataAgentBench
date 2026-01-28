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
    if sym is None:
        continue
    s_symbols.append(sym)
    company_map[sym] = desc

available_symbols = [s for s in s_symbols if s in trade_tables]

parts = []
for s in available_symbols:
    part = "SELECT '" + s + "' AS symbol, SUM(CASE WHEN Date LIKE '2019-%' AND (High - Low) > 0.2 * Low THEN 1 ELSE 0 END) AS cnt FROM \"" + s + "\""
    parts.append(part)

if parts:
    union_sql = "\nUNION ALL\n".join(parts)
    full_sql = "SELECT symbol, cnt FROM (\n" + union_sql + "\n) ORDER BY cnt DESC;"
else:
    full_sql = "SELECT NULL AS symbol, 0 AS cnt WHERE FALSE;"

symbols_info = [{'Symbol': s, 'Company Description': company_map.get(s)} for s in available_symbols]

out = {'symbols_info': symbols_info, 'sql': full_sql}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_QB0CCR1hatdVEWXkYN8q4fGL': 'file_storage/call_QB0CCR1hatdVEWXkYN8q4fGL.json', 'var_call_5zfSoW9T2RnNqppz3xCdHJon': 'file_storage/call_5zfSoW9T2RnNqppz3xCdHJon.json'}

exec(code, env_args)
