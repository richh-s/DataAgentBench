code = """import json
nyse_path = var_call_exRSNvWJaascqpdlppDM9YN5
with open(nyse_path,'r') as f:
    nyse = json.load(f)
nyse_syms = {r['symbol'] for r in nyse}

trade_path = var_call_KRShI0X5inPXfxfej725q4kp
with open(trade_path,'r') as f:
    trade_tables = set(json.load(f))

syms = sorted(nyse_syms & trade_tables)
for bad in ['DD','DO']:
    if bad in syms:
        syms.remove(bad)

parts = []
for s in syms:
    parts.append("SELECT '{s}' AS symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM \"{s}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'".format(s=s))

full_query = "SELECT symbol, up_days, down_days FROM ({u}) WHERE up_days > down_days ORDER BY (up_days - down_days) DESC, up_days DESC LIMIT 5;".format(u=' UNION ALL '.join(parts))

print('__RESULT__:')
print(json.dumps({'n_syms': len(syms), 'query': full_query}))"""

env_args = {'var_call_exRSNvWJaascqpdlppDM9YN5': 'file_storage/call_exRSNvWJaascqpdlppDM9YN5.json', 'var_call_KRShI0X5inPXfxfej725q4kp': 'file_storage/call_KRShI0X5inPXfxfej725q4kp.json', 'var_call_U1ddfDlkeQPeMxPDlffHHSmn': 'file_storage/call_U1ddfDlkeQPeMxPDlffHHSmn.json', 'var_call_e99RdVeKg6vCaWuCanFj7m6f': 'file_storage/call_e99RdVeKg6vCaWuCanFj7m6f.json'}

exec(code, env_args)
