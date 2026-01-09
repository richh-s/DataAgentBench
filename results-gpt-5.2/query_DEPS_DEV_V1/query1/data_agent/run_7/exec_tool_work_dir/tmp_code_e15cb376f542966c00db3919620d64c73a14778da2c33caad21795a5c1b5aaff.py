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

print('__RESULT__:')
print(json.dumps({'ppv_cols': list(ppv_df.columns), 'pkg_cols': list(pkg_df.columns)}))"""

env_args = {'var_call_Z2uGzLu5Ia6ztPh0oPzFXIP7': 'file_storage/call_Z2uGzLu5Ia6ztPh0oPzFXIP7.json', 'var_call_1QGSqqyNDZo8Y66QbYUHuHcC': 'file_storage/call_1QGSqqyNDZo8Y66QbYUHuHcC.json', 'var_call_BNfD7Iir4yoYI4yI3g4ncWcN': 'file_storage/call_BNfD7Iir4yoYI4yI3g4ncWcN.json'}

exec(code, env_args)
