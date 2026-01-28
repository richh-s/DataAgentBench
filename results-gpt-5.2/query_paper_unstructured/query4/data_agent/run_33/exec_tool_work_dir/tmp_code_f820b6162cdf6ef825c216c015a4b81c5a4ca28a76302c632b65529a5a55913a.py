code = """import json
import pandas as pd

def load_maybe_path(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

docs = load_maybe_path(var_call_R9IgLCM12ettU72Jx9kIe7Oo)

# just output filenames to debug
fns = [d.get('filename','') for d in docs[:50]]
print('__RESULT__:')
print(json.dumps(fns, ensure_ascii=False))"""

env_args = {'var_call_R9IgLCM12ettU72Jx9kIe7Oo': 'file_storage/call_R9IgLCM12ettU72Jx9kIe7Oo.json', 'var_call_gUBeyYOL6Gmwdwug8MRO0GZQ': 'file_storage/call_gUBeyYOL6Gmwdwug8MRO0GZQ.json'}

exec(code, env_args)
