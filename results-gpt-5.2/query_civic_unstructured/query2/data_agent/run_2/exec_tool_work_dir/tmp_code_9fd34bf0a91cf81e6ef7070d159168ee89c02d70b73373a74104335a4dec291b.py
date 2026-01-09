code = """import json, pandas as pd

def load_json_maybe_path(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

docs = load_json_maybe_path(var_call_Vtkar1isgHg5NYjEr20jrsBI)

# Filter to 2022 docs by filename containing 2022
sel = [d for d in docs if '2022' in d.get('filename','')]

park_completed_2022 = []
for d in sel:
    text = d.get('text','').lower()
    if 'park' in text and 'completed' in text and '2022' in text:
        park_completed_2022.append(d.get('filename'))

print('__RESULT__:')
print(json.dumps({'n_2022_docs': len(sel), 'n_park_completed_mentions': len(park_completed_2022), 'sample_filenames': park_completed_2022[:20]}))"""

env_args = {'var_call_Vtkar1isgHg5NYjEr20jrsBI': 'file_storage/call_Vtkar1isgHg5NYjEr20jrsBI.json', 'var_call_z3Uc0TUUYnFKnmYOips0lfcE': 'file_storage/call_z3Uc0TUUYnFKnmYOips0lfcE.json', 'var_call_MP61JIGkf4luApqBahtYpPyH': {'ok': True}}

exec(code, env_args)
