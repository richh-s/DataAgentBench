code = """import json, re, pandas as pd

# Load records (may be a path)
rec_src = var_call_GAs27dPaznQA8ZxbA6C6TXE2
if isinstance(rec_src, str):
    with open(rec_src, 'r', encoding='utf-8') as f:
        recs = json.load(f)
else:
    recs = rec_src

def extract_copies(desc: str):
    if desc is None:
        return None
    s = desc.lower()
    # patterns like 'appearing 21 times', 'copied 12 times', 'duplicated 8 times', 'appears 9 times'
    m = re.search(r'(?:appearing|appears|copied|duplicated)\s+(\d+)\s+times', s)
    if m:
        return int(m.group(1))
    return None

for r in recs:
    r['copies'] = extract_copies(r.get('repo_data_description'))

df = pd.DataFrame(recs)
df = df.dropna(subset=['copies'])
# ensure uniqueness by id (id uniquely determines file); take max copies per id
agg = df.groupby('id', as_index=False).agg(
    copies=('copies','max'),
    sample_repo_name=('sample_repo_name','first'),
    sample_path=('sample_path','first')
)
# choose the most frequently copied
agg = agg.sort_values(['copies','id'], ascending=[False, True]).head(1)
res = agg.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_kVKYk57S67g3qtpPsw9aRFq3': [], 'var_call_myikqYIP9LuNtACxuZPYdBco': 'file_storage/call_myikqYIP9LuNtACxuZPYdBco.json', 'var_call_GAs27dPaznQA8ZxbA6C6TXE2': 'file_storage/call_GAs27dPaznQA8ZxbA6C6TXE2.json'}

exec(code, env_args)
