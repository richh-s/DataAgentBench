code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

biz = load_records(var_call_AYyXv9LsIzsqcL0IvI0qZ9In)
biz_df = pd.DataFrame(biz)

pat = re.compile(r"\b([A-Z][A-Za-z .\-']+),\s*([A-Z]{2})\b")

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = pat.search(desc)
    return m.group(2) if m else None

biz_df['state'] = biz_df['description'].map(extract_state)

counts = biz_df['state'].value_counts(dropna=False).head(20)

print('__RESULT__:')
print(json.dumps({'state_value_counts_head': counts.to_dict()}))"""

env_args = {'var_call_AYyXv9LsIzsqcL0IvI0qZ9In': 'file_storage/call_AYyXv9LsIzsqcL0IvI0qZ9In.json', 'var_call_mvUTq4R7LE2uFfV6ZMMwzuo4': 'file_storage/call_mvUTq4R7LE2uFfV6ZMMwzuo4.json'}

exec(code, env_args)
