code = """import json
import pandas as pd

# Load clinical query result from storage
with open(var_call_Aqx3og4knI7XgSyuA3gd75Lf, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# Identify columns
cols = df.columns.tolist()
# Find rows mentioning glioma or LGG
mask_glioma = df.apply(lambda row: row.astype(str).str.contains('glioma', case=False, na=False).any(), axis=1)
mask_brain = df.apply(lambda row: row.astype(str).str.contains('brain', case=False, na=False).any(), axis=1)
mask_lgg = df.apply(lambda row: row.astype(str).str.contains('LGG', case=False, na=False).any(), axis=1)

sample_rows = df[mask_glioma | mask_brain | mask_lgg].head(20).to_dict(orient='records')

result = {
    'columns': cols,
    'num_rows': len(df),
    'glioma_or_brain_matches_count': int((mask_glioma | mask_brain | mask_lgg).sum()),
    'sample_matches': sample_rows
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_CTiuVYQ0GzbevuBkPuuokkjQ': ['clinical_info'], 'var_call_HmLQhigU0Pu3WEKpxZ5We0HE': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_Aqx3og4knI7XgSyuA3gd75Lf': 'file_storage/call_Aqx3og4knI7XgSyuA3gd75Lf.json'}

exec(code, env_args)
