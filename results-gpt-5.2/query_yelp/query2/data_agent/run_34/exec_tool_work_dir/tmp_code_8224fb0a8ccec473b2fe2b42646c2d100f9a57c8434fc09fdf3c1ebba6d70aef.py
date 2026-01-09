code = """import json, re, pandas as pd

def load_tool_result(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

business_records = load_tool_result(var_call_7zTbh6V4tUeyH6N2GC7yXF58)
review_records = load_tool_result(var_call_EeisKdPrtiC9qFaVsr8NuUe9)

bdf = pd.DataFrame(business_records)
rdf = pd.DataFrame(review_records)

pat = re.compile(r",\s*([A-Z]{2})(?:\s|,|\.|\b)")

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    s = desc[:200]
    m = re.search(r"\bin\s+[^,]{1,50},\s*([A-Z]{2})\b", s)
    if m:
        return m.group(1)
    m = pat.search(s)
    if m:
        return m.group(1)
    return None

bdf['state'] = bdf['description'].apply(extract_state)
bdf['review_count'] = pd.to_numeric(bdf['review_count'], errors='coerce')

state_totals = bdf.dropna(subset=['state','review_count']).groupby('state', as_index=False)['review_count'].sum().sort_values('review_count', ascending=False)
top_state = state_totals.iloc[0]['state']

# map ids
bdf['business_ref'] = bdf['business_id'].astype(str).str.replace('businessid_', 'businessref_', regex=False)

rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
per_biz = rdf.dropna(subset=['business_ref','rating']).groupby('business_ref', as_index=False)['rating'].mean().rename(columns={'rating':'biz_avg_rating'})

state_biz = bdf[bdf['state']==top_state][['business_ref']].dropna().drop_duplicates()
merged = state_biz.merge(per_biz, on='business_ref', how='inner')
state_avg_business_rating = float(merged['biz_avg_rating'].mean())

result = {
    'state': top_state,
    'total_reviews_in_state': int(state_totals.iloc[0]['review_count']),
    'average_business_rating_in_state': round(state_avg_business_rating, 4),
    'num_businesses_with_reviews_used_for_avg': int(len(merged))
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_7zTbh6V4tUeyH6N2GC7yXF58': 'file_storage/call_7zTbh6V4tUeyH6N2GC7yXF58.json', 'var_call_EeisKdPrtiC9qFaVsr8NuUe9': 'file_storage/call_EeisKdPrtiC9qFaVsr8NuUe9.json', 'var_call_FvfNnOOuSlINA493fLZYfR3x': {'state': None, 'total_reviews_in_state': None, 'average_business_rating_in_state': None, 'num_businesses_with_reviews_used_for_avg': 0}, 'var_call_kxgWkk4eTFILLzRGwWhC7XXQ': {'top_state_values': {'PA': 27, 'FL': 23, 'IN': 12, 'MO': 9, 'LA': 7, 'AB': 4, 'ID': 4, 'CA': 3, 'IL': 3, 'TN': 3, 'NJ': 2, 'NV': 2, 'AZ': 1}}}

exec(code, env_args)
