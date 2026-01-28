code = """import json
import pandas as pd
# load storage variables
stockinfo = pd.read_json(var_call_NkPP1Uxj8LfaOPgtJPN6p56u)
trade_tables = pd.read_json(var_call_1h3tI42bKR1cchwSgT4gHyna)
# extract symbols from stockinfo
symbols = stockinfo['Symbol'].astype(str).tolist()
# trade_tables is a list
trade_list = trade_tables.tolist()
# intersect
symbols_in_trade = [s for s in symbols if s in trade_list]
# prepare mapping from symbol to company description
sym2desc = dict(zip(stockinfo['Symbol'], stockinfo['Company Description']))
# create list of dicts
out = {'symbols': symbols_in_trade, 'sym2desc': sym2desc}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_NkPP1Uxj8LfaOPgtJPN6p56u': 'file_storage/call_NkPP1Uxj8LfaOPgtJPN6p56u.json', 'var_call_1h3tI42bKR1cchwSgT4gHyna': 'file_storage/call_1h3tI42bKR1cchwSgT4gHyna.json'}

exec(code, env_args)
