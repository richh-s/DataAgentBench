code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

biz = pd.DataFrame(load_records(var_call_IXRsmvUPODRIJr7mp4l2uQsP))
rev = pd.DataFrame(load_records(var_call_K6dAAbajJ8oQTnQ4Clt9GAZ7))

# Parse state from description: pattern ', ST,'
pat = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if desc is None:
        return None
    m = pat.findall(desc)
    # choose the last 2-letter token; typically city, ST
    return m[-1] if m else None

biz['state'] = biz['description'].map(extract_state)
biz['review_count'] = pd.to_numeric(biz['review_count'], errors='coerce').fillna(0).astype(int)

state_reviews = biz.groupby('state', dropna=True)['review_count'].sum().sort_values(ascending=False)
if state_reviews.empty:
    result = {"state": None, "total_reviews": 0, "avg_rating": None}
else:
    top_state = state_reviews.index[0]
    total_reviews = int(state_reviews.iloc[0])

    # map businessref_x -> businessid_x
    rev['business_id'] = rev['business_ref'].astype(str).str.replace('businessref_', 'businessid_', regex=False)
    rev['rating'] = pd.to_numeric(rev['rating'], errors='coerce')

    top_biz_ids = set(biz.loc[biz['state'] == top_state, 'business_id'].astype(str))
    top_rev = rev[rev['business_id'].isin(top_biz_ids) & rev['rating'].notna()]
    avg_rating = float(top_rev['rating'].mean()) if len(top_rev) else None
    result = {"state": top_state, "total_reviews": total_reviews, "avg_rating": None if avg_rating is None else round(avg_rating, 3)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_IXRsmvUPODRIJr7mp4l2uQsP': 'file_storage/call_IXRsmvUPODRIJr7mp4l2uQsP.json', 'var_call_K6dAAbajJ8oQTnQ4Clt9GAZ7': 'file_storage/call_K6dAAbajJ8oQTnQ4Clt9GAZ7.json'}

exec(code, env_args)
