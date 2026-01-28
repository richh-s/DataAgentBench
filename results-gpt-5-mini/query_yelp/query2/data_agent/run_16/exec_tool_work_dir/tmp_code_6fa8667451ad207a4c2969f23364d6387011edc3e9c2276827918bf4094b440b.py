code = """import json
import pandas as pd
import re

with open(var_call_jZEL08NkDEmjwOrm2hls2Id8, 'r') as f:
    businesses = json.load(f)
with open(var_call_VHSQ4WPpBD7ghRgUueDxfic2, 'r') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)

# ensure description
df_b['description'] = df_b.get('description', pd.Series([None]*len(df_b))).astype(str)

# patterns
p1 = re.compile(r'in\s+[^,]+,\s*([A-Z]{2})\b')
q = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    m1 = p1.search(desc)
    if m1:
        return m1.group(1)
    m2 = q.search(desc)
    if m2:
        return m2.group(1)
    return None

sample = []
for i,row in df_b.head(200).iterrows():
    desc = row['description']
    st1 = extract_state(desc)
    sample.append({'business_id': row.get('business_id'), 'description': desc, 'state_extracted': st1})

res = {'total_businesses': len(df_b), 'sample_count': len(sample), 'sample': sample}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_jZEL08NkDEmjwOrm2hls2Id8': 'file_storage/call_jZEL08NkDEmjwOrm2hls2Id8.json', 'var_call_VHSQ4WPpBD7ghRgUueDxfic2': 'file_storage/call_VHSQ4WPpBD7ghRgUueDxfic2.json', 'var_call_5RpQqoTcTOoukUzuaAJIcCgW': {'state': None, 'total_reviews': 0, 'avg_review_rating': None, 'avg_business_rating': None}}

exec(code, env_args)
