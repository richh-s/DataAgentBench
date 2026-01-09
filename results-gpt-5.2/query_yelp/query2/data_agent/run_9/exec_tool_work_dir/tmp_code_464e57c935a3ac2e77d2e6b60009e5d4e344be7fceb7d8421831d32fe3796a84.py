code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

biz = load_records(var_call_0FCafEWNzDCyxFVfMTQjn1fl)

dfb = pd.DataFrame(biz)
pat = re.compile(r',\s*([A-Z]{2})\b')

def get_state(desc):
    if not isinstance(desc, str):
        return None
    m = pat.findall(desc)
    return m[-1] if m else None

dfb['state'] = dfb['description'].map(get_state)
dfb['review_count_num'] = pd.to_numeric(dfb['review_count'], errors='coerce')

out = {
    "n_rows": int(len(dfb)),
    "n_state_nonnull": int(dfb['state'].notna().sum()),
    "sample_states": dfb['state'].dropna().unique()[:20].tolist(),
    "review_count_null": int(dfb['review_count_num'].isna().sum()),
    "review_count_min": None if dfb['review_count_num'].dropna().empty else float(dfb['review_count_num'].min()),
    "review_count_max": None if dfb['review_count_num'].dropna().empty else float(dfb['review_count_num'].max()),
    "sample_desc": dfb['description'].dropna().head(5).tolist()
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0FCafEWNzDCyxFVfMTQjn1fl': 'file_storage/call_0FCafEWNzDCyxFVfMTQjn1fl.json', 'var_call_d2B8rtRoEAk1d7rH7WdBrch3': 'file_storage/call_d2B8rtRoEAk1d7rH7WdBrch3.json', 'var_call_ILw30yE0blAuVTLXSApnwEqn': {'error': 'No state/review_count data parsed'}}

exec(code, env_args)
