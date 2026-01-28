code = """import json, re
import pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

biz = load_records(var_call_lEVLORx38Xvma2ftRdz1gNQM)
rev = load_records(var_call_YdRnGsHpbvKBiUVsFSopv0aa)

dfb = pd.DataFrame(biz)
dfr = pd.DataFrame(rev)

# Parse state abbreviation from description like "in City, ST," or "in City, ST location"
pattern = re.compile(r"\b([A-Z][A-Za-z .'-]+),\s*([A-Z]{2})\b")

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = pattern.search(desc)
    if m:
        return m.group(2)
    return None

dfb['state'] = dfb['description'].apply(extract_state)
# numeric review_count
for col in ['review_count']:
    dfb[col] = pd.to_numeric(dfb[col], errors='coerce')

# map businessid_# -> businessref_#
dfb['business_ref'] = dfb['business_id'].astype(str).str.replace('businessid_', 'businessref_', regex=False)

# join reviews to business state
joined = dfr.merge(dfb[['business_ref','state']], on='business_ref', how='left')
joined['rating'] = pd.to_numeric(joined['rating'], errors='coerce')

# total number of reviews per state
state_counts = joined.dropna(subset=['state']).groupby('state', as_index=False).agg(
    review_count=('rating','count'),
    avg_rating=('rating','mean')
)
state_counts = state_counts.sort_values(['review_count','avg_rating'], ascending=[False, False])

top = state_counts.iloc[0].to_dict() if len(state_counts) else {}
# format avg_rating to 2 decimals
if top:
    top['avg_rating'] = round(float(top['avg_rating']), 2)
    top['review_count'] = int(top['review_count'])

result = top
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_lEVLORx38Xvma2ftRdz1gNQM': 'file_storage/call_lEVLORx38Xvma2ftRdz1gNQM.json', 'var_call_YdRnGsHpbvKBiUVsFSopv0aa': 'file_storage/call_YdRnGsHpbvKBiUVsFSopv0aa.json'}

exec(code, env_args)
