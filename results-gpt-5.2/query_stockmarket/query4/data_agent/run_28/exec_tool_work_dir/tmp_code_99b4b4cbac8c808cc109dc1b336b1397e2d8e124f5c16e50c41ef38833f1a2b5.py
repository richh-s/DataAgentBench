code = """import json, pandas as pd
v=var_call_8Rmh6nq21wxXn4UkriQTxNnE
info=json.load(open(v)) if isinstance(v,str) else v
info_df=pd.DataFrame(info)
print('__RESULT__:')
print(json.dumps({'contains_DHI': bool((info_df.Symbol=='DHI').any()), 'contains_GES': bool((info_df.Symbol=='GES').any())}))"""

env_args = {'var_call_8Rmh6nq21wxXn4UkriQTxNnE': 'file_storage/call_8Rmh6nq21wxXn4UkriQTxNnE.json', 'var_call_53fSB6wCGArWqzaRLsIKLcr4': 'file_storage/call_53fSB6wCGArWqzaRLsIKLcr4.json', 'var_call_fgUZlAnSreN5Yh3kqwKzCzRT': 'file_storage/call_fgUZlAnSreN5Yh3kqwKzCzRT.json', 'var_call_7UpfW7yFAS8XXLPO6POIvZU0': {'n_sqls': 2, 'n_symbols': 234}, 'var_call_x9AcRZPOnYc0zbV9uGogn3CO': 'file_storage/call_x9AcRZPOnYc0zbV9uGogn3CO.json', 'var_call_PEKBnicfP7D5IzgYJ430Do2F': {'DHI': False, 'sample_similar': ['DHS']}, 'var_call_0AgBu3VLbHl54zOMLbvvx2ow': {'n_info': 234, 'n_trade_tables': 2753, 'n_good': 234, 'missing_from_trade_tables': [], 'max_len_symbol': 4}}

exec(code, env_args)
