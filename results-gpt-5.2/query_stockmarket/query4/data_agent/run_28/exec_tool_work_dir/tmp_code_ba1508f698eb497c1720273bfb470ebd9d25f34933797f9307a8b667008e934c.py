code = """import json, pandas as pd

# load info list from sqlite query
v=var_call_8Rmh6nq21wxXn4UkriQTxNnE
info=json.load(open(v)) if isinstance(v,str) else v
info_df=pd.DataFrame(info)

# load trade tables
v2=var_call_53fSB6wCGArWqzaRLsIKLcr4
tables=json.load(open(v2)) if isinstance(v2,str) else v2
trade_set=set(tables)

# normalize symbols by stripping possible whitespace
info_df['Symbol']=info_df['Symbol'].astype(str).str.strip()

# intersect only
good=sorted(set(info_df['Symbol']).intersection(trade_set))

# sanity check some known missing from errors
missing=[s for s in ['DHI','GES','DB','KSU'] if s in set(info_df['Symbol']) and s not in trade_set]

print('__RESULT__:')
print(json.dumps({'n_info': len(info_df), 'n_trade_tables': len(trade_set), 'n_good': len(good), 'missing_from_trade_tables': missing, 'max_len_symbol': max(len(s) for s in good)}))"""

env_args = {'var_call_8Rmh6nq21wxXn4UkriQTxNnE': 'file_storage/call_8Rmh6nq21wxXn4UkriQTxNnE.json', 'var_call_53fSB6wCGArWqzaRLsIKLcr4': 'file_storage/call_53fSB6wCGArWqzaRLsIKLcr4.json', 'var_call_fgUZlAnSreN5Yh3kqwKzCzRT': 'file_storage/call_fgUZlAnSreN5Yh3kqwKzCzRT.json', 'var_call_7UpfW7yFAS8XXLPO6POIvZU0': {'n_sqls': 2, 'n_symbols': 234}, 'var_call_x9AcRZPOnYc0zbV9uGogn3CO': 'file_storage/call_x9AcRZPOnYc0zbV9uGogn3CO.json', 'var_call_PEKBnicfP7D5IzgYJ430Do2F': {'DHI': False, 'sample_similar': ['DHS']}}

exec(code, env_args)
