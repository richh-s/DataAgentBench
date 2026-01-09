code = """import json, pandas as pd
path_cit = var_call_lQPvr4jLWcuGx4GMacVkBaZm
with open(path_cit, 'r', encoding='utf-8') as f:
    cits = json.load(f)

df = pd.DataFrame(cits)
info = {'columns': list(df.columns), 'head': df.head(3).to_dict(orient='records')}
print('__RESULT__:')
print(json.dumps(info))"""

env_args = {'var_call_TfX9M9enUCk4BvRhLnewUTBq': 'file_storage/call_TfX9M9enUCk4BvRhLnewUTBq.json', 'var_call_lQPvr4jLWcuGx4GMacVkBaZm': 'file_storage/call_lQPvr4jLWcuGx4GMacVkBaZm.json', 'var_call_bcXU1gAR7JWAJROBDk0vKr2G': 'file_storage/call_bcXU1gAR7JWAJROBDk0vKr2G.json'}

exec(code, env_args)
