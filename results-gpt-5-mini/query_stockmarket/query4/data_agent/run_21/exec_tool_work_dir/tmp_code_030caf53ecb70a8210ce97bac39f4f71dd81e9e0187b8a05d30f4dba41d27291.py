code = """import json
with open(var_call_rRmEOQdBJdvZ2MWsGvcVRR1D, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_TNNo3PG04ccYq62LaQbnWW9w, 'r') as f:
    trade_tables = json.load(f)
symbols = [rec['Symbol'] for rec in stockinfo]
trade_set = set(trade_tables)
symbols_in_trade = [s for s in symbols if s in trade_set]
print("__RESULT__:")
print(json.dumps(symbols_in_trade))"""

env_args = {'var_call_rRmEOQdBJdvZ2MWsGvcVRR1D': 'file_storage/call_rRmEOQdBJdvZ2MWsGvcVRR1D.json', 'var_call_TNNo3PG04ccYq62LaQbnWW9w': 'file_storage/call_TNNo3PG04ccYq62LaQbnWW9w.json'}

exec(code, env_args)
