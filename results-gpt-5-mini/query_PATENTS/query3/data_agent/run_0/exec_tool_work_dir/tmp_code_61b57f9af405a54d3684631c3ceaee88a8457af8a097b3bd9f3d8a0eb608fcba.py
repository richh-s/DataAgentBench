code = """import json
path = var_call_QqRXYIisemYrUlTibJ8VYOlC
with open(path, 'r') as f:
    data = json.load(f)
out = []
for r in data:
    name = r.get('assignee','')
    if not name:
        continue
    if name.upper() == 'UNIV CALIFORNIA':
        continue
    if any(name.startswith(pref) for pref in ('US-','EP-','WO-','JP-','KR-','TW-','CN-','FR-','DE-','ID-')):
        continue
    out.append({'assignee': name, 'cpc_titles': r.get('cpc_titles')})

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_6Kreubw6sda70vrL4hVhh4Px': ['publicationinfo'], 'var_call_c23BeMWTAwQXdF8yov9bBp9t': ['cpc_definition'], 'var_call_l55xEibBEPLvcbgsB4ym2Tu7': 'file_storage/call_l55xEibBEPLvcbgsB4ym2Tu7.json', 'var_call_F0XFlqDiYITWL1MBYbrkembO': 'file_storage/call_F0XFlqDiYITWL1MBYbrkembO.json', 'var_call_lRNyp9wRymrVkIyIL4PoXol6': 'file_storage/call_lRNyp9wRymrVkIyIL4PoXol6.json', 'var_call_QqRXYIisemYrUlTibJ8VYOlC': 'file_storage/call_QqRXYIisemYrUlTibJ8VYOlC.json'}

exec(code, env_args)
