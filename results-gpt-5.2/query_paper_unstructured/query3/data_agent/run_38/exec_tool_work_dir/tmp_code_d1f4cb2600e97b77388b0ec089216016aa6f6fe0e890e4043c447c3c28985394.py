code = """import json
import pandas as pd

path_cit = var_call_pJUoBOD4gzic997sxqFXbYgW
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)

df = pd.DataFrame(cit)
print('__RESULT__:')
print(json.dumps({'columns': df.columns.tolist(), 'head': df.head(5).to_dict(orient='records')}))"""

env_args = {'var_call_F6F7FPlZguD3C8fO9BEXO9cQ': 'file_storage/call_F6F7FPlZguD3C8fO9BEXO9cQ.json', 'var_call_pJUoBOD4gzic997sxqFXbYgW': 'file_storage/call_pJUoBOD4gzic997sxqFXbYgW.json', 'var_call_fctWhpzPaIUkV7suRLsL7LGk': 'file_storage/call_fctWhpzPaIUkV7suRLsL7LGk.json'}

exec(code, env_args)
