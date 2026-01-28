code = """import pandas as pd, json, os
result_file = locals()['var_functions.query_db:0']
if isinstance(result_file, str) and os.path.exists(result_file):
    with open(result_file, 'r') as f:
        etf_symbols = json.load(f)
else:
    etf_symbols = result_file

df_etf_symbols = pd.DataFrame(etf_symbols)
print('__RESULT__:')
print(json.dumps({'count': len(df_etf_symbols), 'head': df_etf_symbols.head(10).to_dict(orient='records')}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
