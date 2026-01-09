code = """import json, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pkg = load_records(var_call_Z2uGzLu5Ia6ztPh0oPzFXIP7)
ppv = load_records(var_call_1QGSqqyNDZo8Y66QbYUHuHcC)

pkg_df = pd.DataFrame(pkg)
ppv_df = pd.DataFrame(ppv)

pkg_df['UpstreamPublishedAt'] = pd.to_numeric(pkg_df['UpstreamPublishedAt'], errors='coerce')
latest_df = (pkg_df.sort_values(['Name','UpstreamPublishedAt','Version'])
             .groupby('Name', as_index=False)
             .tail(1)
             .loc[:, ['Name','Version','UpstreamPublishedAt']]
             .copy())
latest_df['System'] = 'NPM'

j = latest_df.merge(ppv_df, on=['System','Name','Version'], how='inner')

print('__RESULT__:')
print(json.dumps({'j_cols': list(j.columns), 'j_head': j.head(3).to_dict(orient='records')}))"""

env_args = {'var_call_Z2uGzLu5Ia6ztPh0oPzFXIP7': 'file_storage/call_Z2uGzLu5Ia6ztPh0oPzFXIP7.json', 'var_call_1QGSqqyNDZo8Y66QbYUHuHcC': 'file_storage/call_1QGSqqyNDZo8Y66QbYUHuHcC.json', 'var_call_BNfD7Iir4yoYI4yI3g4ncWcN': 'file_storage/call_BNfD7Iir4yoYI4yI3g4ncWcN.json', 'var_call_H34KjCVgIe3d3GiJKx7oftTE': {'ppv_cols': ['System', 'Name', 'Version', 'ProjectName'], 'pkg_cols': ['Name', 'Version', 'UpstreamPublishedAt']}}

exec(code, env_args)
