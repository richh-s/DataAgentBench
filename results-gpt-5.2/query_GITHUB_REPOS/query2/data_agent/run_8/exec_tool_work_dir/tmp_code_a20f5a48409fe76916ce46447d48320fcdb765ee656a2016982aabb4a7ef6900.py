code = """import json, pandas as pd

# load full result
path = var_call_aY972KLlJaJ6ntEKavgegGmv
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# keep non-binary swift files based on repo_data_description containing 'non-binary'
df = df[df['repo_data_description'].str.lower().str.contains('non-binary', na=False)].copy()
# parse copies as int
pd.set_option('mode.chained_assignment', None)
df['copies'] = pd.to_numeric(df['copies_str'], errors='coerce')
df = df.dropna(subset=['copies'])
df['copies'] = df['copies'].astype(int)

# ensure each file uniquely by id: take max copies per id (should be same), and take a representative repo/path
agg = df.sort_values(['copies'], ascending=False).groupby('id', as_index=False).agg(
    copies=('copies','max'),
    sample_repo_name=('sample_repo_name','first'),
    sample_path=('sample_path','first')
)

# find top copied file id
max_copies = agg['copies'].max() if len(agg) else None
top = agg[agg['copies'] == max_copies].sort_values(['sample_repo_name','sample_path','id']).to_dict(orient='records')

out = {
    'max_copies': int(max_copies) if max_copies is not None else None,
    'top_files': top[:20],
    'top_file_count_ties': int(len(top))
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_bpHHydKI678fGXsdb7U5N4gw': [], 'var_call_jTnpIdz9HwPXjYKH32EPdCzZ': 'file_storage/call_jTnpIdz9HwPXjYKH32EPdCzZ.json', 'var_call_aY972KLlJaJ6ntEKavgegGmv': 'file_storage/call_aY972KLlJaJ6ntEKavgegGmv.json'}

exec(code, env_args)
