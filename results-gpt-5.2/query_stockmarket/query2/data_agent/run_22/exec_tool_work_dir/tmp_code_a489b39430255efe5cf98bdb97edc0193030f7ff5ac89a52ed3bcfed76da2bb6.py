code = """import json, pandas as pd

info = var_call_wgw92BVAntb683am8PU9CuoP
if isinstance(info, str):
    with open(info, 'r') as f:
        info = json.load(f)
trade_tables = var_call_1ua2Y7QX3q0bbYnH7DZgKC2b
if isinstance(trade_tables, str):
    with open(trade_tables, 'r') as f:
        trade_tables = json.load(f)

etf_df = pd.DataFrame(info)
etf_symbols = sorted(set(etf_df['symbol']).intersection(trade_tables))

# Determine symbols requiring quoting (non-alphanumeric/underscore)
import re
needs_quote = [s for s in etf_symbols if re.search(r'[^A-Za-z0-9_]', s)]

print('__RESULT__:')
print(json.dumps({'num_candidate_etfs': len(etf_symbols), 'num_needs_quote': len(needs_quote), 'examples_needs_quote': needs_quote[:20]}))"""

env_args = {'var_call_wgw92BVAntb683am8PU9CuoP': 'file_storage/call_wgw92BVAntb683am8PU9CuoP.json', 'var_call_1ua2Y7QX3q0bbYnH7DZgKC2b': 'file_storage/call_1ua2Y7QX3q0bbYnH7DZgKC2b.json', 'var_call_LcZdQORHsdFywW8kfXLs8ogr': {'test': 'ok'}, 'var_call_Xfvd67ZxRXS1nJxPeBIqrjpb': 'file_storage/call_Xfvd67ZxRXS1nJxPeBIqrjpb.json', 'var_call_s7asqScoZqD7HnSZF7Y06mHX': []}

exec(code, env_args)
