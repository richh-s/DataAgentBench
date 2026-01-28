code = """import json
import pandas as pd
# load storage variables
stockinfo = pd.read_json(var_call_NkPP1Uxj8LfaOPgtJPN6p56u)
trade_tables = pd.read_json(var_call_1h3tI42bKR1cchwSgT4gHyna)
# extract symbols from stockinfo
symbols = stockinfo['Symbol'].astype(str).tolist()
# trade_tables is a DataFrame with single column? convert to list
if isinstance(trade_tables, pd.DataFrame):
    trade_list = trade_tables.iloc[:,0].astype(str).tolist()
else:
    trade_list = list(trade_tables)
# intersect
symbols_in_trade = [s for s in symbols if s in trade_list]
# prepare mapping from symbol to company description
sym2desc = dict(zip(stockinfo['Symbol'], stockinfo['Company Description']))
# create list of dicts
out = {'symbols_count': len(symbols_in_trade), 'symbols_head': symbols_in_trade[:20], 'sym2desc_sample': {k: sym2desc[k] for k in symbols_in_trade[:20]}}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_NkPP1Uxj8LfaOPgtJPN6p56u': 'file_storage/call_NkPP1Uxj8LfaOPgtJPN6p56u.json', 'var_call_1h3tI42bKR1cchwSgT4gHyna': 'file_storage/call_1h3tI42bKR1cchwSgT4gHyna.json'}

exec(code, env_args)
