code = """import json
with open(var_call_JJXAp8DK6M2yHvYQPNfOY1bj, 'r') as f:
    stockinfo_records = json.load(f)
stockinfo_syms = [r['Symbol'] for r in stockinfo_records]
with open(var_call_Cvbmm6EWb3LxORAAoWskYzKl, 'r') as f:
    trade_tables = json.load(f)
trade_set = set(trade_tables)
common = sorted([s for s in stockinfo_syms if s in trade_set])

# Build SQL union all to get max adj close in 2015 for each symbol
parts = []
for s in common:
    # safe quoting of symbol as identifier by double quotes, and as literal in select
    part = f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
    parts.append(part)
sql = '\nUNION ALL\n'.join(parts) + '\n;'

out = {'num_symbols': len(common), 'sql': sql[:100000]}  # include first 100k chars to avoid huge print
# But we also need full SQL for next step; write to a temp file and return its path
with open('/tmp/full_sql_query.sql', 'w') as f:
    f.write(sql)
out['sql_file'] = '/tmp/full_sql_query.sql'
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_JJXAp8DK6M2yHvYQPNfOY1bj': 'file_storage/call_JJXAp8DK6M2yHvYQPNfOY1bj.json', 'var_call_Cvbmm6EWb3LxORAAoWskYzKl': 'file_storage/call_Cvbmm6EWb3LxORAAoWskYzKl.json', 'var_call_4hB7aYbKGVhVFJEMTYgli7zH': {'num_etfs_in_stockinfo': 1435, 'num_tables_in_trade_db': 2753, 'num_common_symbols': 1435, 'has_SPY': True, 'sample_common_first_20': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}}

exec(code, env_args)
