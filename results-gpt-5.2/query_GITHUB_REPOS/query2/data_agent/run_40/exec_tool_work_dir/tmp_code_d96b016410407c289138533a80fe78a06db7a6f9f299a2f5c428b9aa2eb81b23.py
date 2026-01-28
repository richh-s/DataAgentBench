code = """import json, re
import pandas as pd

# load contents result
path_contents = var_call_Vba3PlDwViqAdURZjhOmaseE
with open(path_contents, 'r', encoding='utf-8') as f:
    contents = json.load(f)

df = pd.DataFrame(contents)

# parse copies count from repo_data_description
pat = re.compile(r'(?:duplicated|appearing|appears|seen|repeated|copied)\s+(\d+)\s+times', re.I)

def parse_copies(s):
    if not isinstance(s, str):
        return None
    m = pat.search(s)
    if not m:
        return None
    return int(m.group(1))

df['copies'] = df['repo_data_description'].map(parse_copies)

# Keep rows that clearly have a copies count
df2 = df.dropna(subset=['copies']).copy()

# determine maximum copied file id (uniquely by id)
max_copies = int(df2['copies'].max()) if len(df2) else None

df_max = df2[df2['copies'] == max_copies].copy()

# if multiple ids tie, choose the one with lexicographically smallest id (deterministic)
df_max = df_max.sort_values(['id','sample_repo_name','sample_path']).reset_index(drop=True)

best = df_max.iloc[0].to_dict() if len(df_max) else None

out = {
    'max_copies': max_copies,
    'file_id': best.get('id') if best else None,
    'repository': best.get('sample_repo_name') if best else None,
    'path': best.get('sample_path') if best else None,
    'repo_data_description': best.get('repo_data_description') if best else None,
    'ties_count': int(df_max['id'].nunique()) if best else 0
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Vba3PlDwViqAdURZjhOmaseE': 'file_storage/call_Vba3PlDwViqAdURZjhOmaseE.json', 'var_call_e9oaFymoaXndN3mZfAJVyz7w': 'file_storage/call_e9oaFymoaXndN3mZfAJVyz7w.json'}

exec(code, env_args)
