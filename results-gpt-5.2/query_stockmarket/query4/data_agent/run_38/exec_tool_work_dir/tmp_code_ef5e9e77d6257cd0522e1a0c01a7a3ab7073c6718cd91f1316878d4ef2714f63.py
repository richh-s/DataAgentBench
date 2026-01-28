code = """import json, pandas as pd, math

def to_df(x):
    return pd.DataFrame(x)

keys = [
 'var_call_y8ZCABh432G1gI4a5XxSUdux',
 'var_call_DVXEXqHXG6DAar0IObRZqRWF',
 'var_call_F3klwSrV8vtP1koKskOc8GOc',
 'var_call_kYCWc3Pqhc0eEQ2wjHBqbWL1',
 'var_call_poF9lsj5Kntfvheykf2x0uvu',
 'var_call_Tgmt8xdPR7FHE8XH7R7FJ6Lf',
 'var_call_qeIIIE6saYA4jUk8hA1Gc5fv',
 'var_call_IaInBL9jHCiEcWOS5mNwFiLr'
]
frames=[]
for k in keys:
    v=globals()[k]
    df=to_df(v)
    frames.append(df)
all_df=pd.concat(frames, ignore_index=True)
# coerce numeric
for c in ['up_days','down_days']:
    all_df[c]=pd.to_numeric(all_df[c], errors='coerce')
res=all_df.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_55L71prOlGZnGjPd875JYVlS': 'file_storage/call_55L71prOlGZnGjPd875JYVlS.json', 'var_call_yxBJaU3hRrVIBDsSsWUQyRxF': 'file_storage/call_yxBJaU3hRrVIBDsSsWUQyRxF.json', 'var_call_M01LlNsqnyJUUQ9eBPPgmDJV': {'n_symbols': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_call_ensRNZiRIFvPXFTC9TasurAX': {'n_symbols': 234, 'n_chunks': 6, 'chunk_sizes': [40, 40, 40, 40, 40, 34]}, 'var_call_y8ZCABh432G1gI4a5XxSUdux': [{'symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_DVXEXqHXG6DAar0IObRZqRWF': [{'symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}], 'var_call_F3klwSrV8vtP1koKskOc8GOc': [{'symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}], 'var_call_kYCWc3Pqhc0eEQ2wjHBqbWL1': [{'symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_poF9lsj5Kntfvheykf2x0uvu': [{'symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}], 'var_call_Tgmt8xdPR7FHE8XH7R7FJ6Lf': [{'symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}], 'var_call_qeIIIE6saYA4jUk8hA1Gc5fv': [{'symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}], 'var_call_IaInBL9jHCiEcWOS5mNwFiLr': [{'symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}]}

exec(code, env_args)
