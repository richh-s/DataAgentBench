code = """import json, re, pandas as pd

with open(var_call_TYbPGRaoMBk7OwWbo5ParjQQ, 'r') as f:
    business_records = json.load(f)
with open(var_call_m8ZMyNTj3oieBpizA5sh4sYn, 'r') as f:
    review_records = json.load(f)

bdf = pd.DataFrame(business_records)
rdf = pd.DataFrame(review_records)

state_pattern = re.compile(r',\s*([A-Z]{2})\b')

states = []
for desc in bdf['description'].fillna(''):
    m = state_pattern.search(desc)
    states.append(m.group(1) if m else None)

bdf['state'] = states
bdf['business_ref'] = bdf['business_id'].str.replace('businessid_', 'businessref_', regex=False)

rdf['rating'] = rdf['rating'].astype(float)
merged = rdf.merge(bdf[['business_ref', 'state']], on='business_ref', how='left')
merged = merged[merged['state'].notna()]

agg = merged.groupby('state').agg(review_count=('rating','size'), avg_rating=('rating','mean')).reset_index()

if len(agg) == 0:
    result = {
        'state_with_most_reviews': None,
        'number_of_reviews': 0,
        'average_rating_in_state': None
    }
else:
    top = agg.sort_values('review_count', ascending=False).iloc[0]
    result = {
        'state_with_most_reviews': top['state'],
        'number_of_reviews': int(top['review_count']),
        'average_rating_in_state': round(float(top['avg_rating']), 3)
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_TYbPGRaoMBk7OwWbo5ParjQQ': 'file_storage/call_TYbPGRaoMBk7OwWbo5ParjQQ.json', 'var_call_m8ZMyNTj3oieBpizA5sh4sYn': 'file_storage/call_m8ZMyNTj3oieBpizA5sh4sYn.json'}

exec(code, env_args)
