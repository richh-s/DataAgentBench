code = """import json

# load paths
etf_path = var_call_ASxqUidKouxirPTsX6kyMaGX
trade_path = var_call_qDAxo3HVUHPjQPFy7oZgucv5

with open(etf_path,'r') as f:
    etfs = json.load(f)
with open(trade_path,'r') as f:
    trade_tables = json.load(f)

etf_symbols = sorted({r['Symbol'] for r in etfs})
trade_set = set(trade_tables)
common = [s for s in etf_symbols if s in trade_set]

out = {'etf_count': len(etf_symbols), 'common_count': len(common)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ASxqUidKouxirPTsX6kyMaGX': 'file_storage/call_ASxqUidKouxirPTsX6kyMaGX.json', 'var_call_qDAxo3HVUHPjQPFy7oZgucv5': 'file_storage/call_qDAxo3HVUHPjQPFy7oZgucv5.json', 'var_call_tVCECwffNXINpFAgd099c7UH': [{'x': 'DUMMY'}], 'var_call_91jccmvZMcEWEuAJAsaVFqm0': [{'Date': '1993-01-29', 'Open': '43.96875', 'High': '43.96875', 'Low': '43.75', 'Close': '43.9375', 'Adj Close': '26.299287796020508', 'Volume': '1003200'}], 'var_call_fPP4wsWWGtNhqAp74CX0913q': {'ok': True}, 'var_call_OeauaWLzzwAZ4VeVCRjyphIK': {'type': "<class 'str'>", 'is_str': True}, 'var_call_QaMBbeQYGGpHjYpVDuLX7TjV': {'type': "<class 'str'>", 'is_str': True}}

exec(code, env_args)
