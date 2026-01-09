code = """import json, pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

ppv = load_records(var_call_ARjOrtyN7tkr12WKKpms1n3O)
ppv_df = pd.DataFrame(ppv)
print('__RESULT__:')
print(json.dumps({'columns': list(ppv_df.columns)[:50], 'ncols': len(ppv_df.columns), 'sample': ppv_df.head(3).to_dict(orient='records')}))"""

env_args = {'var_call_g1fm6eUvyVnnJpURKPCqQdKj': 'file_storage/call_g1fm6eUvyVnnJpURKPCqQdKj.json', 'var_call_ARjOrtyN7tkr12WKKpms1n3O': 'file_storage/call_ARjOrtyN7tkr12WKKpms1n3O.json', 'var_call_wflmjMBsRVXEHklUWMBHxqGH': 'file_storage/call_wflmjMBsRVXEHklUWMBHxqGH.json'}

exec(code, env_args)
