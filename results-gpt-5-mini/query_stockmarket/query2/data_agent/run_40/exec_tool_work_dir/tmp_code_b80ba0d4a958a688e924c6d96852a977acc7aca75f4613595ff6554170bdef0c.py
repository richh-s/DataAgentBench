code = """import json
with open(var_call_uujsuC1CCLMoXiLygvLHw84R, 'r') as f:
    stockinfo_etfs = json.load(f)
with open(var_call_NMGGKIDoDKAikS77E1C3am3R, 'r') as f:
    trade_tables = json.load(f)

etf_symbols = [rec['Symbol'] for rec in stockinfo_etfs]
symbols_in_trade_db = [s for s in etf_symbols if s in trade_tables]

# Prepare result
result = {'symbols_in_trade_db': symbols_in_trade_db, 'count': len(symbols_in_trade_db)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Xbn6LlMeaJI4TuDuO6U1lrKA': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_call_uujsuC1CCLMoXiLygvLHw84R': 'file_storage/call_uujsuC1CCLMoXiLygvLHw84R.json', 'var_call_NMGGKIDoDKAikS77E1C3am3R': 'file_storage/call_NMGGKIDoDKAikS77E1C3am3R.json'}

exec(code, env_args)
