code = """import json
# load the previous execute_python output which contains symbols and descriptions
fn = var_call_N4LMQAANlnNwmoz7cJSdm7gW
with open(fn, 'r') as f:
    data = json.load(f)
symbols = data['symbols']
# build union all SQL
parts = []
for s in symbols:
    # safe table name quoting
    parts.append(f"SELECT '{s}' AS Symbol, COUNT(*) AS cnt FROM \"{s}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (\"High\" - \"Low\") > 0.2 * \"Low\"")
sql = '\nUNION ALL\n'.join(parts) + '\nORDER BY cnt DESC LIMIT 5;'
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_obofffwTil0kays857PB0osJ': 'file_storage/call_obofffwTil0kays857PB0osJ.json', 'var_call_GWxju3cF897Xt8p4q6hk2Rmi': 'file_storage/call_GWxju3cF897Xt8p4q6hk2Rmi.json', 'var_call_N4LMQAANlnNwmoz7cJSdm7gW': 'file_storage/call_N4LMQAANlnNwmoz7cJSdm7gW.json', 'var_call_77byU4CkUXpGTf3PtUNC8hYk': {'num_symbols': 86, 'symbols_count_preview': 86, 'first_10_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}}

exec(code, env_args)
