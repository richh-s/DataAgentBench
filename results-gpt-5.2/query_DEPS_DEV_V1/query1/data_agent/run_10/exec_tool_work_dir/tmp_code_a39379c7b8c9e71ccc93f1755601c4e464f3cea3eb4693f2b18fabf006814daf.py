code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

latest = load_records(var_call_g1fm6eUvyVnnJpURKPCqQdKj)
ppv = load_records(var_call_ARjOrtyN7tkr12WKKpms1n3O)

latest_df = pd.DataFrame(latest)
ppv_df = pd.DataFrame(ppv)
merged = latest_df.merge(ppv_df, on=['System','Name','Version'], how='inner')
print('__RESULT__:')
print(json.dumps({'merged_cols': list(merged.columns), 'head': merged.head(3).to_dict(orient='records')}))"""

env_args = {'var_call_g1fm6eUvyVnnJpURKPCqQdKj': 'file_storage/call_g1fm6eUvyVnnJpURKPCqQdKj.json', 'var_call_ARjOrtyN7tkr12WKKpms1n3O': 'file_storage/call_ARjOrtyN7tkr12WKKpms1n3O.json', 'var_call_wflmjMBsRVXEHklUWMBHxqGH': 'file_storage/call_wflmjMBsRVXEHklUWMBHxqGH.json', 'var_call_IBrNSDvMfnv3jfKQamNJ8heQ': {'columns': ['System', 'Name', 'Version', 'ProjectName'], 'ncols': 4, 'sample': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}]}}

exec(code, env_args)
