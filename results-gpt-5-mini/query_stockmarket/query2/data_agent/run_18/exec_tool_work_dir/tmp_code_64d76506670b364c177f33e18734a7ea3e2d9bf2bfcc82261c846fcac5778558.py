code = """import json
path_etfs = var_call_UpHwLqrnxP6jMvmuilhtHEYp
path_tables = var_call_HViMBQGu5fIjjUvgP8uMwvKu

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

etf_records = load_json(path_etfs)
table_list = load_json(path_tables)

etf_symbols = [r['Symbol'] for r in etf_records]
common = sorted([s for s in etf_symbols if s in table_list])

parts = []
for s in common:
    part = f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
    parts.append(part)

if parts:
    sql = '\nUNION ALL\n'.join(parts) + '\nORDER BY Symbol;'
else:
    sql = ''

output = {'sql': sql, 'num_symbols_in_query': len(common)}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_UpHwLqrnxP6jMvmuilhtHEYp': 'file_storage/call_UpHwLqrnxP6jMvmuilhtHEYp.json', 'var_call_HViMBQGu5fIjjUvgP8uMwvKu': 'file_storage/call_HViMBQGu5fIjjUvgP8uMwvKu.json'}

exec(code, env_args)
