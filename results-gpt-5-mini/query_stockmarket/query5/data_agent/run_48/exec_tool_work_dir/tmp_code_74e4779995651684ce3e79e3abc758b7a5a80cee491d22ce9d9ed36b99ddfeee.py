code = """import json
# Load available symbols from previous storage
with open(var_call_T5JxIIzn9gW9I1SYPaYm57Rh, 'r') as f:
    data = json.load(f)
available_symbols = data['available_symbols']

# Build union SQL
parts = []
for s in available_symbols:
    part = "SELECT '" + s + "' AS symbol, SUM(CASE WHEN Date LIKE '2019-%' AND (High - Low) > 0.2 * Low THEN 1 ELSE 0 END) AS cnt FROM \"" + s + "\""
    parts.append(part)

if parts:
    union_sql = "\nUNION ALL\n".join(parts)
    full_sql = "SELECT symbol, SUM(cnt) AS total FROM (\n" + union_sql + "\n) AS t GROUP BY symbol ORDER BY total DESC LIMIT 5;"
else:
    full_sql = "SELECT NULL AS symbol, 0 AS total WHERE FALSE;"

out = {'sql': full_sql}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_QB0CCR1hatdVEWXkYN8q4fGL': 'file_storage/call_QB0CCR1hatdVEWXkYN8q4fGL.json', 'var_call_5zfSoW9T2RnNqppz3xCdHJon': 'file_storage/call_5zfSoW9T2RnNqppz3xCdHJon.json', 'var_call_T5JxIIzn9gW9I1SYPaYm57Rh': 'file_storage/call_T5JxIIzn9gW9I1SYPaYm57Rh.json'}

exec(code, env_args)
