code = """import json, re, pandas as pd

def load_tool_result(var):
    # var is either a list (already loaded) or a file path string
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

business_records = load_tool_result(var_call_7zTbh6V4tUeyH6N2GC7yXF58)
review_records = load_tool_result(var_call_EeisKdPrtiC9qFaVsr8NuUe9)

bdf = pd.DataFrame(business_records)
rdf = pd.DataFrame(review_records)

# Extract state abbreviation from description like "in City, ST" or "in City, ST," or "in City, ST."
pat = re.compile(r"\b([A-Z]{2})\b")
# Focus on the 'in <city>, <ST' pattern to reduce false matches
pat2 = re.compile(r"\bin\s+[^,]+,\s*([A-Z]{2})\b")

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = pat2.search(desc)
    if m:
        return m.group(1)
    # fallback: if contains ', ST' near the beginning
    m2 = re.search(r",\s*([A-Z]{2})\b", desc)
    if m2:
        return m2.group(1)
    return None

bdf['state'] = bdf['description'].apply(extract_state)
# ensure review_count numeric
bdf['review_count'] = pd.to_numeric(bdf['review_count'], errors='coerce')

# total reviews per state from business metadata
state_totals = bdf.dropna(subset=['state','review_count']).groupby('state', as_index=False)['review_count'].sum()
state_totals = state_totals.sort_values('review_count', ascending=False)
top_state = state_totals.iloc[0]['state'] if len(state_totals) else None

def b_to_r(bid):
    if isinstance(bid, str) and bid.startswith('businessid_'):
        return 'businessref_' + bid.split('businessid_',1)[1]
    return None

bdf['business_ref'] = bdf['business_id'].apply(b_to_r)

# Average rating of businesses in that state: compute per-business average rating from review table, then average across businesses in state
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
per_biz = rdf.dropna(subset=['business_ref','rating']).groupby('business_ref', as_index=False)['rating'].mean().rename(columns={'rating':'biz_avg_rating'})

state_biz = bdf[bdf['state']==top_state][['business_ref']].dropna().drop_duplicates()
merged = state_biz.merge(per_biz, on='business_ref', how='inner')
state_avg_business_rating = float(merged['biz_avg_rating'].mean()) if len(merged) else None

result = {
    'state': top_state,
    'total_reviews_in_state': int(state_totals.iloc[0]['review_count']) if top_state is not None else None,
    'average_business_rating_in_state': None if state_avg_business_rating is None else round(state_avg_business_rating, 4),
    'num_businesses_with_reviews_used_for_avg': int(len(merged))
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_7zTbh6V4tUeyH6N2GC7yXF58': 'file_storage/call_7zTbh6V4tUeyH6N2GC7yXF58.json', 'var_call_EeisKdPrtiC9qFaVsr8NuUe9': 'file_storage/call_EeisKdPrtiC9qFaVsr8NuUe9.json'}

exec(code, env_args)
