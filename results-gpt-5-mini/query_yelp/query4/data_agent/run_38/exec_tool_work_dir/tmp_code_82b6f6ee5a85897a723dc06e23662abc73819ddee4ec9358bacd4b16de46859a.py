code = """import json
import pandas as pd
with open(var_call_O9KyZjGrIpkwN2nC1wIjqtqU,'r') as f:
    businesses = json.load(f)

df = pd.DataFrame(businesses)
# Show columns and counts
cols = list(df.columns)
col_counts = {c: int(df[c].notna().sum()) for c in cols}
# Count categories non-empty
cats_present = 0
if 'categories' in df.columns:
    def has_cat(x):
        if x is None: return False
        if isinstance(x, list): return len([i for i in x if i])>0
        if isinstance(x, str):
            return x.strip().lower()!='none' and x.strip()!=''
        return False
    cats_present = int(df['categories'].apply(has_cat).sum())

# Count attributes present
attrs_present = int(df['attributes'].notna().sum())

res = {'columns': cols, 'col_counts': col_counts, 'categories_nonempty_count': cats_present, 'attributes_nonempty_count': attrs_present, 'total_businesses': len(df)}
import json
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_hXzUi1HOyrj3924Zuuu4nlzl': ['business', 'checkin'], 'var_call_Vx7f3xeQCmMRh0NWNG3HKaZW': ['review', 'tip', 'user'], 'var_call_O9KyZjGrIpkwN2nC1wIjqtqU': 'file_storage/call_O9KyZjGrIpkwN2nC1wIjqtqU.json', 'var_call_VFqrAgjYogQR7lq5ElNsE2Jt': 'file_storage/call_VFqrAgjYogQR7lq5ElNsE2Jt.json', 'var_call_HPQ5bAnzRSDUt6FM5hMjLm5U': {'category': None, 'business_count': 0, 'average_rating': None}}

exec(code, env_args)
