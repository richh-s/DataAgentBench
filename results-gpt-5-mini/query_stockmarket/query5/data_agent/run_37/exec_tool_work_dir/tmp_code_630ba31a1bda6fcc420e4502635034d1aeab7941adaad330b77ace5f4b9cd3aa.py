code = """import json
with open(var_call_VqxF3xG5XGRmxZHnEI5CHGMJ, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_sOBRWuxkOyvJlDzcPXen5MsU, 'r') as f:
    trade_tables = json.load(f)

symbol_to_company = {rec['Symbol'].upper(): rec.get('Company Description','') for rec in stockinfo}
trade_set = set([t.upper() for t in trade_tables])
symbols = sorted([s for s in symbol_to_company.keys() if s in trade_set])

out = {'num_symbols': len(symbols), 'symbols_preview': symbols[:50]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_VqxF3xG5XGRmxZHnEI5CHGMJ': 'file_storage/call_VqxF3xG5XGRmxZHnEI5CHGMJ.json', 'var_call_sOBRWuxkOyvJlDzcPXen5MsU': 'file_storage/call_sOBRWuxkOyvJlDzcPXen5MsU.json', 'var_call_5cuTBpqGleEMyWZK9EI5Ao9X': 'file_storage/call_5cuTBpqGleEMyWZK9EI5Ao9X.json', 'var_call_koNAOQ6bHLQBEVitand5U4Nq': 'file_storage/call_koNAOQ6bHLQBEVitand5U4Nq.json'}

exec(code, env_args)
