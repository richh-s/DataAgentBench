code = """import json, pandas as pd

# reconstruct symbols list
p = var_call_fssuB9N5FSr9mC6JQ02Vi5f3
if isinstance(p, str) and p.endswith('.json'):
    with open(p,'r') as f:
        nyse = json.load(f)
else:
    nyse = p
nyse_df = pd.DataFrame(nyse)

trade_p = var_call_iNc1jtCKZc3PmhFsHF5mVkiw
if isinstance(trade_p, str) and trade_p.endswith('.json'):
    with open(trade_p,'r') as f:
        trade_syms = set(json.load(f))
else:
    trade_syms = set(trade_p)

symbols = sorted(set(nyse_df['Symbol']).intersection(trade_syms))
chunks = [symbols[i:i+80] for i in range(0,len(symbols),80)]
print('__RESULT__:')
print(json.dumps({'chunks': chunks}))"""

env_args = {'var_call_iNc1jtCKZc3PmhFsHF5mVkiw': 'file_storage/call_iNc1jtCKZc3PmhFsHF5mVkiw.json', 'var_call_fssuB9N5FSr9mC6JQ02Vi5f3': 'file_storage/call_fssuB9N5FSr9mC6JQ02Vi5f3.json', 'var_call_scQUSoQgorDdt7RRqHvv1xhe': {'n_symbols': 234, 'n_chunks': 3, 'first_chunk': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_call_SfM57ULaL3Q9PV3FPhhJiKaY': {'n_symbols': 234, 'n_chunks': 3, 'first_chunk': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_call_LMYhEN9DYDrgXoSXb4p2Iz94': [{'up_days': '0', 'down_days': 'nan'}], 'var_call_PrmBMZlBJnqqEpXh4THe6fPl': [{'up_days': '244', 'down_days': '101.0'}], 'var_call_AejerGDszNWjqxDCEHcSWS4p': [{'up_days': '246', 'down_days': '128.0'}], 'var_call_3uQSjgfa4FkZUQVsnMuWJyAx': [{'up_days': '0', 'down_days': 'nan'}], 'var_call_YKxXo0OgNatnqrH7cAfPHMZR': [{'up_days': '246', 'down_days': '123.0'}]}

exec(code, env_args)
